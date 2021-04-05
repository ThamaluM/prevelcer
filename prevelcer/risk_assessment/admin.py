from django.contrib import admin
from .models import RiskScale
# Register your models here.



# Register your models here.
class RiskScaleAdmin(admin.ModelAdmin):
    list_display = ('patient',)

admin.site.register(RiskScale, RiskScaleAdmin)

