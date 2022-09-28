from django.db import models


class categoria(models.Model):
    nome_categoria = models.CharField(max_length=30, null=False)
    desc_categoria = models.TextField(null=False)

    def __str__(self):
        return self.nome_categoria
