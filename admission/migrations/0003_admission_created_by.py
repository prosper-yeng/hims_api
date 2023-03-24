# Generated by Django 4.0.5 on 2023-01-28 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("admission", "0002_remove_admission_attendance_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="admission",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
