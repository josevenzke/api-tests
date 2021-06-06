from .models import ModifyStr
from rest_framework import serializers

class ModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModifyStr
        fields = '__all__'