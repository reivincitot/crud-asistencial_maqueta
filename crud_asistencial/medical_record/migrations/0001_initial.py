# Generated by Django 4.2.16 on 2024-11-23 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_at_visit', models.PositiveIntegerField(blank=True, help_text='Edad del paciente al momento de la atención', null=True)),
                ('allergies', models.TextField(blank=True, help_text='Listado de alergias', null=True)),
                ('treatments', models.TextField(blank=True, help_text='Historial de tratamientos', null=True)),
                ('exams', models.TextField(blank=True, help_text='Resultado de exámenes médicos', null=True)),
                ('vital_signs', models.JSONField(blank=True, help_text='Signos vitales registrados', null=True)),
                ('blood_type', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medical_record', to='registro.patient')),
            ],
            options={
                'verbose_name': 'Ficha Médica',
                'verbose_name_plural': 'Fichas Médicas',
            },
        ),
    ]