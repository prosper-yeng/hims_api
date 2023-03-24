# Generated by Django 4.0.5 on 2023-03-07 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_patient_hospital_record_no'),
        ('admission', '0008_remove_admission_consultation_diagnosis_and_more'),
        ('treatment_plan', '0008_alter_treatmentplan_objectives'),
        ('need_type', '0002_remove_needtype_nurses_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='needtype',
            name='admission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admission_needtype', to='admission.admission'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='needtype',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patient_needtype', to='person.patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='needtype',
            name='treatment_plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_plan_needtype', to='treatment_plan.treatmentplan'),
            preserve_default=False,
        ),
    ]
