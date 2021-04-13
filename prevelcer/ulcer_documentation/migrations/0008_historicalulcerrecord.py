# Generated by Django 3.1.1 on 2021-04-13 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import ulcer_documentation.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ulcer_documentation', '0007_ulcerrecord_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUlcerRecord',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('last_update', models.DateTimeField(blank=True, editable=False)),
                ('site', models.CharField(choices=[('back_of_head', 'Back of Head'), ('forehead', 'Forehead'), ('right_shoulder', 'Right Shoulder'), ('left_shoulder', 'Left Shoulder'), ('right_heel', 'Right Heel'), ('left_heel', 'Left Heel'), ('left_elbow', 'Left Elbow'), ('right_elbow', 'Right Elbow'), ('right_buttock', 'Right Buttock'), ('left_buttock', 'Left Buttock'), ('right_knee', 'Right Knee'), ('left_knee', 'Left Knee'), ('left_hip', 'Left Hip'), ('right_hip', 'Right Hip'), ('fingers', 'Fingers'), ('toes', 'Toes'), ('other', 'Other')], max_length=50)),
                ('stage', models.CharField(choices=[('I', 'Stage I'), ('II', 'Stage II'), ('III', 'Stage III'), ('IV', 'Stage IV'), ('DTI', 'Deep Tissue Injury'), ('UN', 'Unstaged')], max_length=20)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('depth', models.FloatField()),
                ('margin', models.CharField(choices=[('reg', 'Regular'), ('irreg', 'Irregular')], max_length=8)),
                ('edge', models.CharField(choices=[('sloping', 'Sloping'), ('punched_out', 'Punched out'), ('rollout', 'Rollout'), ('everted', 'Everted')], max_length=20)),
                ('edge_color', models.CharField(max_length=50)),
                ('underminings', models.BooleanField(default=False)),
                ('sinus_tracts', models.BooleanField(default=False)),
                ('floor', ulcer_documentation.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[('healthy', 'Healthy'), ('granulation', 'Granualation Tissue'), ('slough', 'Slough'), ('necrotic', 'Necrotic'), ('eschar', 'Eschar'), ('epithelial', 'Epithelial')], max_length=50), size=6)),
                ('discharge', models.CharField(blank=True, choices=[('serous', 'Serous'), ('purulent', 'Purulent'), ('serosanguineous', 'Serosanguineous'), ('other', 'Other')], max_length=50, null=True)),
                ('discharge_amount', models.CharField(blank=True, choices=[('s', 'Small'), ('m', 'Medium'), ('h', 'Heavy')], max_length=50, null=True)),
                ('surrounding_skin', ulcer_documentation.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[('warm', 'Warm'), ('thickend', 'Thickend'), ('hyperpigmented', 'Hyperpigmented'), ('hypopignmented', 'Hypopignmented'), ('gangrenous', 'Gangreous'), ('itching', 'Itching'), ('swelling', 'Swelling')], max_length=50), size=5)),
                ('skin_sensation', models.CharField(choices=[('g', 'Good'), ('b', 'Impaired')], max_length=50)),
                ('regional_lymph_nodes_enlarged', models.BooleanField(default=False)),
                ('smell', models.BooleanField(default=False)),
                ('pain', models.BooleanField(default=False)),
                ('progress', models.CharField(choices=[('improved', 'Improved'), ('no_change', 'No Change'), ('stable', 'Stable'), ('declined', 'Declined')], max_length=50)),
                ('image', models.TextField(blank=True, max_length=100, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('reported_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ulcer record',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]