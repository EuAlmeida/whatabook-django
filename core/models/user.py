from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField


class user(AbstractUser):
    tip_choices = (
        ("A", "Administrador"),
        ("U", "Usúario Padrão"),
        ("E", "Editora"),
    )

    id_usuario = models.AutoField(primary_key=True)
    data_nasc = models.DateField(blank=True, null=True)
    telefone_user = models.CharField(max_length=11, blank=True)
    endereco_user = models.CharField(max_length=100, blank=True)
    cpf = CPFField("cpf",blank=True)
    foto_perfil = models.ImageField(upload_to="fotoperfil/", blank=True)   
    class Meta:
        verbose_name_plural = "Usuarios"

