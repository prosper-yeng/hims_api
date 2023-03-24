# Generated by Django 4.0.5 on 2023-01-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("status", "0001_initial"),
        ("lab_test", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LabTestPrice",
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
                    "cost_price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "discount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "profit_margin",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "vat",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "other_tax",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("is_deleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lab_test_price_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "lab_test",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lab_test_with_price",
                        to="lab_test.labtest",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lab_test_with_status",
                        to="status.status",
                    ),
                ),
            ],
        ),
    ]
