# Generated by Django 3.1.1 on 2021-04-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assessment', '0002_auto_20210406_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskscale',
            name='venus_thrombosis',
            field=models.BooleanField(default=False),
        ),
    ]
