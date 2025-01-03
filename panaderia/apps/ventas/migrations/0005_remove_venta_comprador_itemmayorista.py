# Generated by Django 5.1.2 on 2024-11-03 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_mayorista', '0006_rename_codicioniva_clientemayorista_condicioniva'),
        ('ventas', '0004_alter_venta_comprador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='comprador',
        ),
        migrations.CreateModel(
            name='ItemMayorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_mayorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente_mayorista.clientemayorista')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta')),
            ],
        ),
    ]
