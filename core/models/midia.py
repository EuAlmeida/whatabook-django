from django.db import models
from django.contrib.auth import get_user_model

class midia(models.Model):
    imagem = models.ImageField(upload_to="images/")
    iduser = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)