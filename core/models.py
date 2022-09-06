from tabnanny import verbose
from django.db import models

class livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo_livro = models.CharField(max_length=100)
    sinopse_livro = models.TextField(null=False)
    qtd_paginas = models.PositiveIntegerField(null=False)
    ano_lancamento = models.DateField(null=False)
    url_compra = models.URLField(null=False)
    

    def __str__(self):
        return self.titulo_livro

class user(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=60)
    data_nasc = models.DateField(null=False)
    telefone_user = models.PositiveIntegerField(null=False)
    endereco_usuario = models.CharField(max_length=100, null=False)
    cpf = models.PositiveIntegerField(null=False)
    email_user = models.EmailField(null=False)
    senha_user = models.CharField(max_length=20)
    adm = models.BooleanField(null=False)

    def __str__(self):
        return self.nome_usuario

class categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, null=False)
    nome_categoria = models.CharField(max_length=30, null=False)
    desc_categoria = models.TextField(null=False)

class autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nome_autor = models.CharField(max_length=60, null=False)
    desc_autor = models.TextField()
    autor_nasc = models.DateField(null=False)
    autor_falecimento = models.DateField(null=True)

    def __str__(self):
        return self.nome_autor
    class Meta:
        verbose_name_plural = "Autores"





