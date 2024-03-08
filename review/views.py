from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from review.models import List
from review.serializer import Serializer


class ReviewView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data["reviewer"] = request.user.id
        data["section"] = kwargs.get("section_id")
        serializer = Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        object = List.objects.filter(section_id=kwargs.get("section_id")).first()
        if object is None:
            raise Http404
        serializer = Serializer(object)
        return Response(serializer.data)