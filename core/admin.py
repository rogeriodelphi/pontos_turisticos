from django.contrib import admin
from rest_framework.viewsets import ModelViewSet

from .models import PontoTuristico

@admin.register(PontoTuristico)
class PontoTuristico(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao', 'aprovado', 'endereco']
