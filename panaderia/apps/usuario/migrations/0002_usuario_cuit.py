# Generated by Django 5.1.2 on 2024-10-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cuit',
            field=models.CharField(default='1234567890', max_length=10, unique=True),
        ),
    ]