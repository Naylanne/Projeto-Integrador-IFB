from django.db import models
from departamento.models import Departamento
from tecnologia.models import Tecnologia


class Projeto(models.Model):
    STATUS_CHOICES = [
        ('Planejado', 'Planejado'),
        ('Em Execução', 'Em Execução'),
        ('Concluido', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]
    
    
    RISCO_CHOICES = [
        ('Baixo', 'Baixo'),
        ('Medio', 'Médio'),
        ('Alto', 'Alto'),
        ('Critico', 'Crítico'),
    ]

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='projetos')
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Planejado')
    risco = models.CharField(
        max_length=50, 
        choices=RISCO_CHOICES, 
        default='Baixo', 
        verbose_name='Nível de Risco'
    )
    orcamento = models.DecimalField(
        max_digits=14, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        verbose_name='Orçamento (R$)'
    )
   
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')

    def __str__(self):
        return self.nome