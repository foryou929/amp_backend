from rest_framework import serializers
from review.models import List


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"