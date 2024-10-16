# Generated by Django 4.0.5 on 2023-01-31 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("consultation_diagnosis", "0002_consultationdiagnosis_patient_type"),
        ("admission", "0004_alter_admission_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="admission",
            name="date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="admission",
            name="consultation_diagnosis",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="consultation_diagnosis_admission",
                to="consultation_diagnosis.consultationdiagnosis",
            ),
            preserve_default=False,
        ),
    ]
