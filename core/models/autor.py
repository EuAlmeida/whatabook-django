from django.db import models


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