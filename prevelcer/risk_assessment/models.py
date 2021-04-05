from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RiskScale(models.Model):

    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )

    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    assessed_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True,related_name="assessed_risk_scale")

    # general

    gender = models.CharField(max_length=2,choices=GENDER_CHOICES,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    height = models.IntegerField(null=True,blank=True)

    # Braden

    sensory_perception = models.IntegerField(null=True,blank=True)
    moisture = models.IntegerField(null=True,blank=True)
    activity = models.IntegerField(null=True,blank=True)
    mobility = models.IntegerField(null=True,blank=True)
    nutrition = models.IntegerField(null=True,blank=True)
    friction_shear = models.IntegerField(null=True,blank=True)


    # risk factors 

    diabetes_mellitus = models.BooleanField(default=False)
    peripheral_vascular_disease = models.BooleanField(default=False)
    cerebral_vascular_accident = models.BooleanField(default=False)
    hypotension = models.BooleanField(default=False)
    hypoalbuminemia = models.BooleanField(default=False)
    incontinence = models.BooleanField(default=False)

    comments = models.CharField(max_length=100,null=True,blank=True)





