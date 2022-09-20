from django.db import models
from .autor import autor
from .categoria import categoria
from .editora import editora

class livro(models.Model):

    id_livro = models.AutoField(primary_key=True)
    titulo_livro = models.CharField(max_length=100)
    sinopse_livro = models.TextField(null=False)
    qtd_paginas = models.PositiveIntegerField(null=False)
    ano_lancamento = models.DateField(null=False)
    url_compra = models.URLField(null=False)
    editora_livro = models.ForeignKey(
        editora, on_delete=models.PROTECT, related_name="livros"
    )
    autor_livros = models.ManyToManyField(autor, related_name="livros")
    categoria_livro = models.ManyToManyField(categoria, related_name="livros")
    capa_livro = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.titulo_livro
