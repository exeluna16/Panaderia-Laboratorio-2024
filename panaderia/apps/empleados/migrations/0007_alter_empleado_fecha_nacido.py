# Generated by Django 5.1.2 on 2024-10-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0006_alter_empleado_cuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacido',
            field=models.DateField(),
        ),
    ]