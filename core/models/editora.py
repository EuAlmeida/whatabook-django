from django.db import models


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
