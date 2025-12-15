from django.db import models

class Tecnologia(models.Model):
    TIPO_CHOICES = [
        ('Linguagem', 'Linguagem'),
        ('Framework', 'Framework'),
        ('Servico Cloud', 'Serviço Cloud'),
        ('Banco de Dados', 'Banco de Dados'),
        ('Outro', 'Outro'),
    ]
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    versao = models.CharField(max_length=50, blank=True, null=True)
    fornecedor = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"