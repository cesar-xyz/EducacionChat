"""EducacionChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import MensajeCreateAPIView, SesionCreateAPIView, TrabajadorCreateAPIView, EmpresaListAPIView, \
    ModuloListAPIView, SucursalListAPIView

# Esquema Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Tu API",
        default_version='v1',
        description="Descripción de tu API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@tuempresa.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Vistas de creación de objetos
    path('mensajes/', MensajeCreateAPIView.as_view(), name='mensaje-create'),
    path('sesiones/', SesionCreateAPIView.as_view(), name='sesion-create'),
    path('trabajadores/', TrabajadorCreateAPIView.as_view(), name='trabajador-create'),

    path('empresas/', EmpresaListAPIView.as_view(), name='empresa-list'),
    path('modulos/', ModuloListAPIView.as_view(), name='modulo-list'),
    path('sucursales/', SucursalListAPIView.as_view(), name='sucursal-list'),

    # Documentación Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
