from django.contrib import admin
from .models import Projeto


class TecnologiasInline(admin.TabularInline):
    model = Projeto.tecnologias.through
    extra = 1 

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'departamento', 'status', 'risco', 'orcamento', 'data_inicio', 'listar_tecnologias')
    
    list_filter = ('status', 'departamento', 'tecnologias', 'risco')
    
    search_fields = ('nome', 'descricao')
    
    ordering = ('-data_inicio',)
    
    fields = (
        'nome', 
        'descricao', 
        'departamento', 
        ('data_inicio', 'data_fim'), 
        'status', 
        ('risco', 'orcamento'), 
    )
    
    readonly_fields = ()

    inlines = [TecnologiasInline]
    
    exclude = ('tecnologias',)

    def listar_tecnologias(self, obj):
        return ", ".join([t.nome for t in obj.tecnologias.all()])
    
    listar_tecnologias.short_description = 'Tecnologias'