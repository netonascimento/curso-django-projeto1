# Generated by Django 4.2.13 on 2024-06-02 03:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projetos", "0004_alter_projetos_data_projeto_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Projetos",
            new_name="Projeto",
        ),
    ]
