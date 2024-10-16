# Generated by Django 4.0.5 on 2023-03-11 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_service_charge', '0001_initial'),
        ('payment_individual', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentindividual',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='paymentindividual',
            name='patient',
        ),
        migrations.AddField(
            model_name='paymentindividual',
            name='patient_service_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payment_of_patient_service_charge', to='patient_service_charge.patientservicecharge'),
            preserve_default=False,
        ),
    ]
