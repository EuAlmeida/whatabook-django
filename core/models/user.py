from django.contrib.auth.models import AbstractUser
from django.db import models



class user(AbstractUser):
    data_nasc = models.DateField(blank=True, null=True)
    telefone_user = models.CharField(max_length=11, blank=True)
    endereco_user = models.CharField(max_length=100, blank=True)
    foto_perfil = models.ImageField(upload_to="fotoperfil/", blank=True)   
    class Meta:
        verbose_name_plural = "Usuarios"


