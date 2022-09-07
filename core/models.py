from tabnanny import verbose
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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

    def __str__(self):
        return self.nome_categoria


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


class editora(models.Model):
    id_editora = models.AutoField(primary_key=True)
    nome_editora = models.CharField(max_length=100, null=False)
    desc_editora = models.TextField()
    cnpj = models.PositiveIntegerField(null=False)
    endereco_editora = models.CharField(max_length=150)
    email_editora = models.EmailField(null=False)
    senha_editora = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome_editora


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

    def __str__(self):
        return self.titulo_livro


class listafav(models.Model):
    id_lista = models.AutoField(primary_key=True)
    titulo_lista = models.CharField(max_length=100, null=False)
    desc_lista = models.TextField(null=False)
    user_lista = models.ForeignKey(user, on_delete=models.PROTECT, related_name="Lista")
    livros_lista = models.ManyToManyField(livro, related_name="lista_livro")



class resenha(models.Model):
    id_lista = models.AutoField(primary_key=True)
    titulo_resenha = models.CharField(max_length=100, null=False)
    desc_resenha = models.TextField(null=False)
    livro_resenha = models.ForeignKey(livro, on_delete=models.PROTECT, related_name="resenha")
    nota_resenha = models.PositiveIntegerField( null=False,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
