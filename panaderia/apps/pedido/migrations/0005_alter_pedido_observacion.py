# Generated by Django 5.1.2 on 2024-11-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_rename_cuit_proveedor_pedido_id_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='observacion',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]