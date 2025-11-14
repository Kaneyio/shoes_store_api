from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_nested import routers
from shoes_store_api.views import MyTokenObtainPairView, ShoeTypeViewSet, ShoeViewSet, AttributesViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Shoe Store API",
        default_version='v1',
        description="Documentação da API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Rotas automáticas (ViewSets)
router = routers.SimpleRouter()
router.register(r'shoe-types', ShoeTypeViewSet)
router.register(r'shoes', ShoeViewSet)

# Rotas aninhadas (atributos de ShoeType)
shoe_type_router = routers.NestedSimpleRouter(router, r'shoe-types', lookup='shoe_type')
shoe_type_router.register(r'attributes', AttributesViewSet, basename='shoe-type-attributes')

# Rotas principais
urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0)),
    path('admin/',  admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(shoe_type_router.urls)),
    path("api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Swagger UI e Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

