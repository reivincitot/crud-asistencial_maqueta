# Generated by Django 4.2.16 on 2024-11-23 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_alter_profesionaldesalud_place_of_origin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.RemoveField(
            model_name='profesionaldesalud',
            name='place_of_origin',
        ),
    ]