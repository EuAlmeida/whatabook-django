# Generated by Django 4.1.1 on 2022-09-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_user_foto_perfil"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="capa_livro",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
