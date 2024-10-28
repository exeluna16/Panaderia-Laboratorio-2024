# Generated by Django 5.1.2 on 2024-10-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('mail', models.EmailField(default='ejemplo@ejemplo.com', max_length=150, null=True)),
                ('tipo_persona', models.CharField(choices=[('FISICA', 'FISICA'), ('JURIDICA', 'JURIDICA')], max_length=20)),
                ('estado', models.BooleanField(default=True)),
                ('calle', models.CharField(max_length=150)),
                ('localidad', models.CharField(max_length=150)),
                ('numero_calle', models.IntegerField(null=True)),
                ('fecha_nacido', models.DateTimeField()),
                ('cuit', models.IntegerField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]