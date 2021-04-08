# Generated by Django 3.1.1 on 2021-04-06 17:04

from django.db import migrations, models
import ulcer_documentation.models


class Migration(migrations.Migration):

    dependencies = [
        ('ulcer_documentation', '0003_auto_20210406_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='ulcerrecord',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ulcerrecord',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ulcerrecord',
            name='progress',
            field=models.CharField(choices=[('improved', 'Improved'), ('no_change', 'No Change'), ('stable', 'Stable'), ('declined', 'Declined')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ulcerrecord',
            name='surrounding_skin',
            field=ulcer_documentation.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[('warm', 'Warm'), ('thickend', 'Thickend'), ('hyperpigmented', 'Hyperpigmented'), ('hypopignmented', 'Hypopignmented'), ('gangrenous', 'Gangreous'), ('itching', 'Itching')], max_length=50), size=5),
        ),
    ]