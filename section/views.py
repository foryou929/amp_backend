from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from section.models import List
from section.serializer import ListSerializer

class MessageView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    def create(self, request, *args, **kwargs):
        # Add foreign key values to request data
        return super().create(request, *args, **kwargs)


class ClientView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    # def get_queryset(self):
    #     queryset = List.objects.filter()
    #     return 


class UserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = "project_id"