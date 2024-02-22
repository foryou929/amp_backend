from rest_framework import serializers
from project.models import List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"

    def to_representation(self, instance):
        processed_data = super().to_representation(instance)
        processed_data["progress_choice"] = instance.get_progress_display()
        return processed_data
