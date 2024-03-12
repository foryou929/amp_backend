from rest_framework import serializers
from section.models import List
from project.models import List as ProjectList
from image.models import List as ImageList
from message.serializer import Serializer as MessageSerializer
from datetime import datetime


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageList
        fields = "__all__"


class ProjectListSerializer(serializers.ModelSerializer):
    project_images = ImageListSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectList
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):
    section_messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = "__all__"
        depth = 1


class SectionListSerializer(serializers.ModelSerializer):
    project = ProjectListSerializer(read_only=True)
    section_messages = MessageSerializer(many=True, read_only=True)
    suggest_count = serializers.IntegerField()
    current = serializers.SerializerMethodField()

    class Meta:
        model = List
        fields = "__all__"
        depth = 1

    def get_current(self, obj):
        return datetime.now()
