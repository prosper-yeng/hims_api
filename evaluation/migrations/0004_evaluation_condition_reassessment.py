# Generated by Django 4.0.5 on 2023-02-24 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='condition_reassessment',
            field=models.BooleanField(default=False),
        ),
    ]
