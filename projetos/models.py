from django.db import models

# Create your models here.


class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=200)
    data_projeto = models.DateTimeField("Data do Projeto")
    descricao_projeto = models.CharField(max_length=200)
    foto_projeto = models.ImageField()

    def __str__(self):
        return self.nome_projeto