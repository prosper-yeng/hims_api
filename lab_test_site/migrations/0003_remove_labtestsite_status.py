# Generated by Django 4.0.5 on 2023-03-21 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_test_site', '0002_alter_labtestsite_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labtestsite',
            name='status',
        ),
    ]
