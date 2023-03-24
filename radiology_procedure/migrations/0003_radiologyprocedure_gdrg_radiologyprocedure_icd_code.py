# Generated by Django 4.0.5 on 2023-03-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiology_procedure', '0002_alter_radiologyprocedure_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiologyprocedure',
            name='gdrg',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='GDRG'),
        ),
        migrations.AddField(
            model_name='radiologyprocedure',
            name='icd_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ICD CODE'),
        ),
    ]
