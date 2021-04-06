# Generated by Django 3.1.1 on 2021-04-05 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=2, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('sensory_perception', models.IntegerField(blank=True, null=True)),
                ('moisture', models.IntegerField(blank=True, null=True)),
                ('activity', models.IntegerField(blank=True, null=True)),
                ('mobility', models.IntegerField(blank=True, null=True)),
                ('nutrition', models.IntegerField(blank=True, null=True)),
                ('friction_shear', models.IntegerField(blank=True, null=True)),
                ('diabetes_mellitus', models.BooleanField(default=False)),
                ('peripheral_vascular_disease', models.BooleanField(default=False)),
                ('cerebral_vascular_accident', models.BooleanField(default=False)),
                ('hypotension', models.BooleanField(default=False)),
                ('hypoalbuminemia', models.BooleanField(default=False)),
                ('incontinence', models.BooleanField(default=False)),
                ('comments', models.CharField(blank=True, max_length=100, null=True)),
                ('assessed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assessed_risk_scale', to=settings.AUTH_USER_MODEL)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]