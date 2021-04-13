from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):

    ADMIN = 0
    PATIENT = 1
    CARER = 2
    DOCTOR = 3
      
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (PATIENT, 'Patient'),
        (CARER, 'Carer'),
        (DOCTOR, 'Doctor')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/profilepictures/', blank=True, null=True)   
    phone_number = models.CharField(max_length=12)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    friends = models.ManyToManyField(User,blank=True,related_name='friends')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



