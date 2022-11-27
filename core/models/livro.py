from django.db import models

from .autor import autor
from .categoria import categoria
from .user import user
from django.contrib.auth import get_user_model


class livro(models.Model):
    titulo_livro = models.CharField(max_length=100)
    sinopse_livro = models.TextField(null=False)
    qtd_paginas = models.PositiveIntegerField(null=False)
    ano_lancamento = models.DateField(null=False)
    url_compra = models.URLField(null=False, max_length=1000)
    editora_livro = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="livros"
    )
    isbn = models.CharField(max_length=30, blank=True)
    autor_livros = models.ManyToManyField(autor, related_name="livros")
    categoria_livro = models.ManyToManyField(categoria, related_name="livros")
    capa_livro = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.titulo_livro
