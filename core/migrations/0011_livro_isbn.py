# Generated by Django 4.1.2 on 2022-11-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_user_cnpj_user_is_editora_alter_livro_editora_livro_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="isbn",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]