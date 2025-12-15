from django.contrib import admin
from .models import Departamento


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'gestor', 'ativo', 'data_criacao')
    
    list_filter = ('ativo',)

    search_fields = ('^nome', '^gestor', 'descricao')

    fields = ('nome', 'gestor', 'descricao', 'ativo')

    readonly_fields = ('data_criacao',)