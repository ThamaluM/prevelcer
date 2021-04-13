from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

    readonly_fields = ["prof_picture"]

    def prof_picture(self,obj):
        return mark_safe('<img src="{url}" width="{width}" />'.format(
            url = obj.picture.url,
            width='100%',
            height=obj.picture.height,
            )
    )

admin.site.register(Profile, ProfileAdmin)