# Generated by Django 4.0.5 on 2023-03-05 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_plan', '0007_alter_treatmentplan_doctor'),
        ('procedure', '0001_initial'),
        ('admission', '0007_alter_admission_date'),
        ('status', '0001_initial'),
        ('doctors_note', '0005_alter_doctorsnote_doctor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('procedure_care', '0006_remove_procedurecare_doctor_procedurecare_nurse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedurecare',
            name='admission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedure_care_admission', to='admission.admission'),
        ),
        migrations.AlterField(
            model_name='procedurecare',
            name='doctor_note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_note_procedure_care', to='doctors_note.doctorsnote'),
        ),
        migrations.AlterField(
            model_name='procedurecare',
            name='nurse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nurse_procedure_care', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='procedurecare',
            name='procedure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedure_procedure_care', to='procedure.procedure'),
        ),
        migrations.AlterField(
            model_name='procedurecare',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_procedure_care', to='status.status'),
        ),
        migrations.AlterField(
            model_name='procedurecare',
            name='treatment_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatment_plan_procedure_care', to='treatment_plan.treatmentplan'),
        ),
    ]
