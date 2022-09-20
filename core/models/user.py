from django.db import models
from cpf_field.models import CPFField


class user(models.Model):
    tip_choices = (
        ("A", "Administrador"),
        ("U", "Usúario Padrão"),
        ("E", "Editora"),
    )

    id_usuario = models.AutoField(primary_key=True)
    nome_user = models.CharField(max_length=60)
    data_nasc = models.DateField(null=False)
    telefone_user = models.CharField(max_length=11, null=False)
    endereco_user = models.CharField(max_length=100, null=False)
    cpf = CPFField("cpf",blank=True)
    email_user = models.EmailField(null=False)
    senha_user = models.CharField(max_length=20)
    tip = models.CharField(max_length=1, null=False, choices=tip_choices)
    foto_perfil = models.ImageField(upload_to="fotoperfil/")

    def __str__(self):
        return self.nome_user
    class Meta:
        verbose_name_plural = "Usuarios"

