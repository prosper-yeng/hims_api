# Generated by Django 4.0.5 on 2023-01-28 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("medication_administration", "0001_initial"),
        ("treatment_plan", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="medicationadministration",
            name="treatment_plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="medication_administration_treatment_plan",
                to="treatment_plan.treatmentplan",
            ),
        ),
    ]
