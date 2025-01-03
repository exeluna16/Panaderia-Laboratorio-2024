# Generated by Django 5.1.2 on 2024-11-03 21:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0008_rename_cantidad_itempedido_cantidad_pedida_and_more'),
        ('proveedores', '0004_remove_proveedor_cuit_proveedor_cuit_cuil_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecepcionPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recepcion', models.DateField(auto_now=True)),
                ('numero_comprobante', models.IntegerField(blank=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('total_pedido', models.DecimalField(decimal_places=2, max_digits=10)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor')),
            ],
        ),
    ]
