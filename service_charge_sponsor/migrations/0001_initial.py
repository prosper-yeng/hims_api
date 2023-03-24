# Generated by Django 4.0.5 on 2023-01-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("service", "0001_initial"),
        ("currency_type", "0001_initial"),
        ("sponsor", "0001_initial"),
        ("status", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceChargeSponsor",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "percentage_allowed",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "currency_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="currency_type.currencytype",
                    ),
                ),
                (
                    "service",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service.service",
                    ),
                ),
                (
                    "sponsor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sponsor.sponsor",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="status.status"
                    ),
                ),
            ],
        ),
    ]
