from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django import forms

# Create your models here.


# Multiple choice selection

class ChoiceArrayField(ArrayField):
    
    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.TypedMultipleChoiceField,
            'choices': self.base_field.choices,
            'coerce': self.base_field.to_python,
            'widget': forms.CheckboxSelectMultiple,
        }
        defaults.update(kwargs)

        return super(ArrayField, self).formfield(**defaults)

class UlcerRecord(models.Model):

    SITE_CHOICES = (
        ('back_of_head', "Back of Head"),
        ('forehead','Forehead'),
        ('right_shoulder','Right Shoulder'),
        ('left_shoulder', 'Left Shoulder'),
        ('right_heel', 'Right Heel'),
        ('left_heel',"Left Heel"),
        ('left_elbow',"Left Elbow"),
        ('right_elbow', "Right Elbow"),
        ('right_buttock',"Right Buttock"),
        ('left_buttock', "Left Buttock"),
        ('right_knee','Right Knee'),
        ("left_knee","Left Knee"),
        ('left_hip',"Left Hip"),
        ('right_hip','Right Hip'),
        ('fingers','Fingers'),
        ('toes','Toes'),
        ('other','Other')
    )

    STAGE_CHOICES = (
        ('I',"Stage I"),
        ("II", "Stage II"),
        ("III","Stage III"),
        ("IV", "Stage IV"),
        ("DTI", "Deep Tissue Injury"),
        ("UN","Unstaged")
    )

    MARGIN_CHOICES = (
        ('reg', 'Regular'),
        ('irreg','Irregular')
    )

    EDGE_CHOICES = (
        ('sloping','Sloping'),
        ('punched_out',"Punched out"),
        ('rollout',"Rollout"),
        ('everted', "Everted") 
    )

    FLOOR_CHOICES = (
        ('healthy', 'Healthy'),
        ('granulation','Granualation Tissue'),
        ('slough','Slough'),
        ('necrotic', 'Necrotic'),
        ('eschar', 'Eschar'),
        ('epithelial','Epithelial')
    )

    DISCHARGE_CHOICES = (
        ('serous','Serous'), 
        ('purulent','Purulent'),
        ('serosanguineous','Serosanguineous'),
        ('other','Other')
    )

    DISCHARGE_AMOUNT_CHOICES = (
        ('s',"Small"),
        ('m',"Medium"),
        ('h',"Heavy")
    )

    SKIN_CHOICES = (
        ('warm',"Warm"),
        ('thickend',"Thickend"),
        ('hyperpigmented',"Hyperpigmented"),
        ('hypopignmented',"Hypopignmented"),
        ('gangrenous',"Gangreous"),
        ('itching','Itching')
    )

    SENSATION_CHOICE = (
        ('g',"Good"),
        ('b', "Impaired")
    )

    PROGRESS_CHOICES = (
        ("improved","Improved"),
        ("no_change","No Change"),
        ("stable","Stable"),
        ("declined","Declined")
    )

    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True,related_name='reported_ulcers')
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)

    site = models.CharField(max_length=50,choices=SITE_CHOICES)

    stage = models.CharField(max_length=20,choices=STAGE_CHOICES)

    duration = models.DurationField(null=True,blank=True)


    length = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()

    margin = models.CharField(max_length=8,choices=MARGIN_CHOICES)

    edge = models.CharField(max_length=20,choices=EDGE_CHOICES)
    edge_color = models.CharField(max_length=50)
    underminings = models.BooleanField(default=False)
    sinus_tracts = models.BooleanField(default=False)
    

    floor = ChoiceArrayField(models.CharField(max_length=50, blank=True ,choices = FLOOR_CHOICES),size=6)

    discharge = models.CharField(max_length=50, choices = DISCHARGE_CHOICES,null=True,blank=True)
    discharge_amount = models.CharField(max_length=50, choices= DISCHARGE_AMOUNT_CHOICES,null=True,blank=True)
    

    surrounding_skin = ChoiceArrayField(models.CharField(max_length=50, blank=True, choices=SKIN_CHOICES),size=5)
    skin_sensation = models.CharField(max_length=50,choices=SENSATION_CHOICE)

    regional_lymph_nodes_enlarged = models.BooleanField(default=False)

    smell = models.BooleanField(default=False)

    pain = models.BooleanField(default=False)

    progress = models.CharField(max_length=50, choices = PROGRESS_CHOICES)

