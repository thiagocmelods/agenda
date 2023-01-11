from django.db import models


class Contatos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    telefone1 = models.CharField(max_length=15, blank=True, null=True)
    telefone2 = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome
