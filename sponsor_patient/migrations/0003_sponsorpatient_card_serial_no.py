# Generated by Django 4.0.5 on 2023-03-24 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor_patient', '0002_sponsorpatient_nhis_serial_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorpatient',
            name='card_serial_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Card Serial Number'),
        ),
    ]
