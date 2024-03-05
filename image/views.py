from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from image.models import List
from image.serializer import Serializer


class ImageUploadView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = Serializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        if kwargs.get("type") == "project":
            request.data["project"] = kwargs.get("id")

        if kwargs.get("type") == "space":
            request.data["space"] = kwargs.get("id")

        return super().create(request, *args, **kwargs)