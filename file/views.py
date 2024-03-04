from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from file.models import List
from file.serializer import Serializer


class FileUploadView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = Serializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        request.data["message"] = kwargs.get("message_id")
        return super().create(request, *args, **kwargs)