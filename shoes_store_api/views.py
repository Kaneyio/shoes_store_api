from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Attributes, ShoeType, Shoe
from .serializers import ShoeTypeSerializer, ShoeSerializer, AttributeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action

class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.attributes.all().delete()

        return super().destroy(request, *args, **kwargs)

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    permission_classes = [IsAuthenticated]

class AttributesViewSet(viewsets.ModelViewSet):
    queryset = Attributes.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["put"], url_path="bulk-upsert")
    def bulk_upsert(self, request, *args, **kwargs):
        shoe_type_id = self.kwargs.get("shoe_type_pk")
        shoe_type = ShoeType.objects.get(id=shoe_type_id)

        created = []
        updated_ids = []

        for attr_data in request.data:
            attr_id = attr_data.get("id")

            if attr_id:
                Attributes.objects.filter(id=attr_id).update(
                    name=attr_data["name"],
                    description=attr_data["description"]
                )
                updated_ids.append(attr_id)
            else:
                created.append(Attributes(
                    name=attr_data["name"],
                    description=attr_data["description"]
                ))

        new_objects = Attributes.objects.bulk_create(created)
        created_ids = [obj.id for obj in new_objects]
        incoming_ids = updated_ids + created_ids
        existing_ids = list(shoe_type.attributes.values_list("id", flat=True))
        to_delete = set(existing_ids) - set(incoming_ids)

        if to_delete:
            Attributes.objects.filter(id__in=to_delete).delete()

        shoe_type.attributes.set(incoming_ids)
        all_objects = Attributes.objects.filter(id__in=incoming_ids)
        serializer = AttributeSerializer(all_objects, many=True)
        return Response(serializer.data, status=200)

class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception:
            return Response({"message": "Usuário ou senha incorretos."}, status=status.HTTP_401_UNAUTHORIZED)