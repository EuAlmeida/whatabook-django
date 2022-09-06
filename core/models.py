from django.db import models

class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo_livro = models.CharField(max_length=100)
    sinopse_livro = models.CharField(max_length=1000, null=False)
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


