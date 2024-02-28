from rest_framework import serializers
from section.models import List
from message.serializer import ListSerializer as MessageSerializer


# class ListSerializer(serializers.ModelSerializer):
#     suggest_count = serializers.IntegerField()

#     class Meta:
#         model = List
#         fields = "__all__"
#         depth = 2


class ReadSerializer(serializers.ModelSerializer):
    section_messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = "__all__"
        depth = 1


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"
