# Generated by Django 4.0.5 on 2023-03-07 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intervention_type', '0002_alter_interventiontype_nurses_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interventiontype',
            name='nurses_note',
        ),
    ]
