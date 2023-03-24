# Generated by Django 4.0.5 on 2023-02-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bed_allocation", "0003_alter_bedallocation_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="bedallocation",
            name="allocated_date",
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name="bedallocation",
            name="deallocated_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
