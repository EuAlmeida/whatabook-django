from django.db import models

class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    sinopse_livro = models.CharField(max_length=1000)
    titulo_livro = models.CharField(max_length=100)
    qtd_paginas = models.PositiveIntegerField()
    ano_lancamento = models.DateField()
    url_compra = models.URLField()

