from django.contrib import admin
from .models import Mattress, PressureEntry
# Register your models here.

class PressureEntryAdmin(admin.ModelAdmin):
    pass
    


# admin.site.register(PressureEntry, PressureEntryAdmin)

class MatressAdmin(admin.ModelAdmin):
    list_display = ('patient',)

admin.site.register(Mattress,MatressAdmin)