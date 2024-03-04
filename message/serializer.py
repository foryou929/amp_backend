from rest_framework import serializers
from message.models import List
from file.serializer import Serializer as FileSerializer


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class ReadSerializer(serializers.ModelSerializer):
    message_files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = "__all__"
        depth = 1
