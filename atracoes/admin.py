from django.contrib import admin
from .models import Atracao

@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao', 'horario_func', 'idade_minima']