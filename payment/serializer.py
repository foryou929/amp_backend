from rest_framework import serializers
from payment.models import List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"
