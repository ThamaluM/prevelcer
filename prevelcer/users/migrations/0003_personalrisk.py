# Generated by Django 3.1.1 on 2020-11-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalRisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
