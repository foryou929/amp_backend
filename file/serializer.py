from rest_framework import serializers
from file.models import List


class CreateSerializer(serializers.ModelSerializer):
    # file = serializers.FileField()

    class meta:
        model = List
        fields = "__all__"
