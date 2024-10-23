# Generated by Django 5.1.2 on 2024-10-23 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('mail', models.EmailField(max_length=150)),
                ('tipo_persona', models.CharField(max_length=20)),
                ('estado', models.BooleanField(default=True)),
                ('calle', models.CharField(max_length=150)),
                ('localidad', models.CharField(max_length=150)),
                ('numero_calle', models.IntegerField(null=True)),
                ('fecha_nacido', models.DateTimeField()),
                ('cuit', models.IntegerField(unique=True)),
                ('fecha_ingreso', models.DateTimeField()),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo', to='empleados.cargo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
