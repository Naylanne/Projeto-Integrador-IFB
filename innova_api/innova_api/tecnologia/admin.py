from django.contrib import admin
from .models import Tecnologia


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'versao', 'fornecedor')
    list_filter = ('tipo', 'fornecedor')
    search_fields = ('nome', 'descricao')
