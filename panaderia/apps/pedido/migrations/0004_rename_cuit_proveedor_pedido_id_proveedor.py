# Generated by Django 5.1.2 on 2024-11-02 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_rename_numero_pedido_numero_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='cuit_proveedor',
            new_name='id_proveedor',
        ),
    ]
