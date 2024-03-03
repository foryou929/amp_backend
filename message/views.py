from utils.views import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from message.models import List
from message.serializer import ListSerializer, ReadSerializer


class MessageView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    read_serializer_class = ReadSerializer
    lookup_field = "section_id"

    def create(self, request, *args, **kwargs):
        request.data["section"] = self.kwargs.get("section_id")
        return super().create(request, *args, **kwargs)
