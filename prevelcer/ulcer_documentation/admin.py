from django.contrib import admin
from .models import UlcerRecord
# Register your models here.

class UlcerRecordAdmin(admin.ModelAdmin):
    
    list_display = ('patient',)
    
admin.site.register(UlcerRecord, UlcerRecordAdmin)

    
