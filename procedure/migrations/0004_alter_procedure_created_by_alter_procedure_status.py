# Generated by Django 4.0.5 on 2023-03-29 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('procedure', '0003_alter_procedure_procedure_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='created_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='procedure_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='status',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='procedure_user', to='status.status'),
        ),
    ]
