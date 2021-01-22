from rest_framework import serializers
from .models import PressureEntry

class PressureEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = PressureEntry
        fields = "__all__"
        