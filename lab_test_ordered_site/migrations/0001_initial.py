# Generated by Django 4.0.5 on 2023-01-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("site_type", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lab_test_order_details", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LabTestOrderedSite",
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
                ("is_deleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Created"),
                            ("approved", "Approved"),
                            ("active", "Active"),
                            ("deactivate", "Deactivate"),
                            ("suspended", "Suspended"),
                            ("delete", "Delete"),
                            ("closed", "Closed"),
                            ("registered", "Registered"),
                            ("vital done", "Vital Done"),
                            ("diagnosed", "Diagnosed"),
                            ("billed", "Billed"),
                            ("pending lab", "Pending Lab"),
                            ("pending pharmacy", "Pending Pharmacy"),
                        ],
                        default="active",
                        max_length=100,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lab_test_ordered_site_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "lab_test_order_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="in_lab_test_ordered_site",
                        to="lab_test_order_details.labtestorderdetails",
                    ),
                ),
                (
                    "site_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="site_type_order_test",
                        to="site_type.sitetype",
                    ),
                ),
            ],
        ),
    ]
