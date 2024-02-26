from rest_framework import serializers
from project.models import List
from section.serializer import ListSerializer as SectionSerializer


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class ProjectSectionSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = "__all__"
