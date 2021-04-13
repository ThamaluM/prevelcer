from django.contrib import admin
from .models import UlcerRecord
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

class UlcerRecordAdmin(SimpleHistoryAdmin):
    
    list_display = ('patient',)
    history_list_display = ('patient','stage','progress')
    
admin.site.register(UlcerRecord, UlcerRecordAdmin)

    
