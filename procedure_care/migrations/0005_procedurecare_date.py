# Generated by Django 4.0.5 on 2023-02-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedure_care', '0004_alter_procedurecare_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedurecare',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
