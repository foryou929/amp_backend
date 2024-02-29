from rest_framework import serializers
from user.models import List

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'