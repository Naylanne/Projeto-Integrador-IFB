from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=200)
    gestor = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome