# Generated by Django 4.1.2 on 2022-11-25 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_livro_medianota_alter_resenha_livro_resenha_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livro",
            name="medianota",
        ),
    ]