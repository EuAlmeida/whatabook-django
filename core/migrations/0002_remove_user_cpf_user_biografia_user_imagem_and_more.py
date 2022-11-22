# Generated by Django 4.1.2 on 2022-11-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="cpf",
        ),
        migrations.AddField(
            model_name="user",
            name="biografia",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="user",
            name="localizacao",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]