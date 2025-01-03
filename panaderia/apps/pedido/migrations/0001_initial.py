# Generated by Django 5.1.2 on 2024-10-26 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fecha_realizado', models.DateTimeField(auto_now_add=True)),
                ('observacion', models.CharField(max_length=150, null=True)),
                ('cuit_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Proveedor', to='proveedores.proveedor')),
            ],
        ),
    ]
