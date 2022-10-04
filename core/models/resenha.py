from django.db import models

from .livro import livro
from .user import user


class resenha(models.Model):
    nota_choices = (
        (1, "1 estrela"),
        (2, "2 estrelas"),
        (3, "3 estrelas"),
        (4, "4 estrelas"),
        (5, "5 estrelas"),
    )

    titulo_resenha = models.CharField(max_length=100, null=False)
    desc_resenha = models.TextField(null=False)
    livro_resenha = models.ForeignKey(
        livro, on_delete=models.PROTECT, related_name="resenha"
    )
    nota_resenha = models.IntegerField(null=False, choices=nota_choices)
    user_resenha = models.ForeignKey(
        user, on_delete=models.PROTECT, related_name="resenha"
    )
    