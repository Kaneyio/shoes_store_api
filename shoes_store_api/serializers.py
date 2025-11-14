from rest_framework import serializers
from .models import ShoeType, Shoe, Attributes

class AttributeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Attributes
    fields = '__all__'

class ShoeTypeSerializer(serializers.ModelSerializer):
  attributes = AttributeSerializer(many=True, read_only=True)
  attributes_ids = serializers.PrimaryKeyRelatedField(
    queryset=Attributes.objects.all(),
    many=True,
    source="attributes",
    write_only=True
  )

  class Meta:
    model = ShoeType
    fields = '__all__'

class ShoeSerializer(serializers.ModelSerializer):
  shoe_type = ShoeTypeSerializer(read_only=True)
  shoe_type_id = serializers.PrimaryKeyRelatedField(
    queryset=ShoeType.objects.all(),
    source="shoe_type",
    write_only=True
  )
  class Meta:
    model = Shoe
    fields = '__all__'