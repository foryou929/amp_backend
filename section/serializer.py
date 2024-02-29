from rest_framework import serializers
from section.models import List
from message.serializer import ListSerializer as MessageSerializer


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = List
        fields = "__all__"
        depth = 1


class ReadSerializer(serializers.ModelSerializer):
    section_messages = MessageSerializer(many=True, read_only=True)
    suggest_count = serializers.IntegerField()

    class Meta:
        model = List
        fields = "__all__"
        depth = 1
