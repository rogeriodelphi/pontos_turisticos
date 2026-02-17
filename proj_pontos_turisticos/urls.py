from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from atracoes.api.viewsets import AtracaoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'pontoturisticos', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'enderecos', EnderecoViewSet, basename='Endereco')
router.register(r'atracoes', AtracaoViewSet, basename='Atracao')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
