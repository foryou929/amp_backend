from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from message.models import List
from message.serializer import Serializer, ReadSerializer


class MessageView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kargs):
        queryset = List.objects.filter(section=kargs.get("section_id"))
        serializer = ReadSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request.data["section"] = kwargs.get("section_id")
        request.data["sender"] = request.user.id
        serializer = Serializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            serializer = ReadSerializer(instance)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
