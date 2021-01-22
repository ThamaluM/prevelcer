from django.db import models
from users.models import User
# Create your models here.

class Mattress(models.Model):
    
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    serial = models.TextField(unique=True)

class PressureEntry(models.Model):

    mat = models.ForeignKey(Mattress, on_delete=models.CASCADE)
    n = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    l_x = models.IntegerField()
    l_y = models.IntegerField()
    p = models.FloatField()

    def as_json(self):
        return dict(
            mat = self.mat.id,
            n = self.n,
            x = self.x,
            y = self.y,
            lx = self.l_x,
            ly = self.l_y,
            p = self.p,
        )


class ReportCycle(models.Model):

    mat = models.ForeignKey(Mattress,  on_delete=models.CASCADE)
    n = models.IntegerField()
    start_dt = models.DateTimeField( auto_now=False, auto_now_add=False)
    end_dt = models.DateTimeField( auto_now=False, auto_now_add=False, blank=True, null = True)


