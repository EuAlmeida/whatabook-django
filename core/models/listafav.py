from django.db import models

from .livro import livro
from .user import user


class listafav(models.Model):
    id_lista = models.AutoField(primary_key=True)
    titulo_lista = models.CharField(max_length=100, null=False)
    desc_lista = models.TextField(null=False)
    user_lista = models.ForeignKey(user, on_delete=models.PROTECT, related_name="Lista")
    livros_lista = models.ManyToManyField(livro, related_name="lista_livro")
