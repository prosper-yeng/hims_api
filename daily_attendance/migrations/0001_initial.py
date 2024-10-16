# Generated by Django 4.0.5 on 2023-01-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("person", "0001_initial"),
        ("clinic_type", "0001_initial"),
        ("relative", "0001_initial"),
        ("sponsor", "0001_initial"),
        ("status", "0001_initial"),
        ("attendance_type", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyAttendanceModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_of_visit",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("OpdNo", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "ccc",
                    models.CharField(
                        blank=True,
                        help_text="This is the claims check code field",
                        max_length=100,
                        null=True,
                    ),
                ),
                ("copay", models.IntegerField(default=0)),
                ("vital_sign_taken", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(default=django.utils.timezone.now)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "attendance_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="attendance_type.attendancetype",
                    ),
                ),
                (
                    "clinic",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clinic_type.clinictype",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="System User",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient_attendance",
                        to="person.patient",
                    ),
                ),
                (
                    "relative",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="relative",
                        to="relative.relative",
                        verbose_name=" Relative",
                    ),
                ),
                (
                    "sponsor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sponsor",
                        to="sponsor.sponsor",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="status_attendance",
                        to="status.status",
                    ),
                ),
            ],
        ),
    ]
