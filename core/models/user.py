from django.db import models
from django.contrib.auth.models import AbstractUser

# from cpf_field.models import CPFField

class user(AbstractUser):
    # cpf = CPFField('cpf')
    telefone = models.CharField(max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    biografia = models.CharField(max_length=200, blank=True, null=True)
    localizacao = models.CharField(max_length=200, blank=True, null=True)

