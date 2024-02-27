from rest_framework import serializers
from project.models import List
from section.serializer import (
    SectionMessageSerializer,
)
from datetime import datetime


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class ReadSerializer(serializers.ModelSerializer):
    current = serializers.SerializerMethodField()

    class Meta:
        model = List
        fields = "__all__"
        depth = 1

    def get_current(self, obj):
        return datetime.now()


class ProjectSectionSerializer(serializers.ModelSerializer):
    sections = SectionMessageSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = "__all__"
