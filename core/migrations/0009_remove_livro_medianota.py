# Generated by Django 4.1.2 on 2022-11-26 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_livro_medianota"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livro",
            name="medianota",
        ),
    ]