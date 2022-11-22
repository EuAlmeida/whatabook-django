# Generated by Django 4.1.2 on 2022-11-22 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_user_cpf_user_biografia_user_imagem_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="imagem",
        ),
        migrations.CreateModel(
            name="midia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imagem", models.ImageField(upload_to="images/")),
                (
                    "iduser",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]