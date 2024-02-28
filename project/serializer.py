from rest_framework import serializers
from project.models import List
from section.serializer import ReadSerializer as SectionReadSerializer
from datetime import datetime


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class ReadSerializer(serializers.ModelSerializer):
    project_sections = SectionReadSerializer(many=True, read_only=True)
    current = serializers.SerializerMethodField()

    class Meta:
        model = List
        fields = "__all__"
        depth = 1

    def get_current(self, obj):
        return datetime.now()
