# Generated by Django 5.1.2 on 2024-10-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_alter_empleado_tipo_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='mail',
            field=models.EmailField(default='ejemplo@ejemplo.com', max_length=150, null=True),
        ),
    ]
