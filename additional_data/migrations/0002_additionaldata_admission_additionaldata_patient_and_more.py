# Generated by Django 4.0.5 on 2023-03-07 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_patient_hospital_record_no'),
        ('admission', '0007_alter_admission_date'),
        ('treatment_plan', '0008_alter_treatmentplan_objectives'),
        ('additional_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaldata',
            name='admission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admission_additional_data', to='admission.admission'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additionaldata',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patient_additional_data', to='person.patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additionaldata',
            name='treatment_plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_plan_additional_data', to='treatment_plan.treatmentplan'),
            preserve_default=False,
        ),
    ]
