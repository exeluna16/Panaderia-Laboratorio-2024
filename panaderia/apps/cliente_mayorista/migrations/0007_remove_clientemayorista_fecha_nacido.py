# Generated by Django 5.1.2 on 2024-11-04 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_mayorista', '0006_rename_codicioniva_clientemayorista_condicioniva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientemayorista',
            name='fecha_nacido',
        ),
    ]
