from rest_framework import serializers
from project.models import List
from section.serializer import Serializer as SectionSerializer
from image.serializer import Serializer as ImageSerializer
from datetime import datetime


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class ReadSerializer(serializers.ModelSerializer):
    project_sections = SectionSerializer(many=True, read_only=True)
    project_images = ImageSerializer(many=True, read_only=True)
    suggest_count = serializers.IntegerField()
    current = serializers.SerializerMethodField()

    class Meta:
        model = List
        fields = "__all__"
        depth = 1

    def get_current(self, obj):
        return datetime.now()
