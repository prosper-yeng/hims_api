# Generated by Django 4.0.5 on 2023-01-31 09:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patient_review", "0002_patientreview_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientreview",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
