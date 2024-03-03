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


# class ClientMessageView(ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = List.objects.all()
#     serializer_class = ListSerializer
# def get_queryset(self):
#     queryset = List.objects.filter()
#     return


# class UserMessageView(ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = List.objects.all()
#     serializer_class = ListSerializer
# def get_queryset(self):
#     section_id = self.kwargs.get('section_id')
#     return List.objects.filter(sender_id=self.request.user, section_id=section_id)
