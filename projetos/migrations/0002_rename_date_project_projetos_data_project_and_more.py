# Generated by Django 4.2.13 on 2024-06-02 03:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projetos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projetos",
            old_name="date_project",
            new_name="data_project",
        ),
        migrations.RenameField(
            model_name="projetos",
            old_name="descripton_project",
            new_name="descricao_project",
        ),
        migrations.RenameField(
            model_name="projetos",
            old_name="endereco_foto",
            new_name="foto_projeto",
        ),
        migrations.RenameField(
            model_name="projetos",
            old_name="name_project",
            new_name="nome_project",
        ),
    ]
