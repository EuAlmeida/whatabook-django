from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)


