# Generated by Django 3.1.1 on 2021-04-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulcer_documentation', '0006_auto_20210407_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='ulcerrecord',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/ulcers/'),
        ),
    ]
