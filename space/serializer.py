from rest_framework import serializers
from space.models import List
from image.serializer import Serializer as ImageSerializer


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class ReadSerializer(serializers.ModelSerializer):
    space_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = "__all__"
        depth = 1
