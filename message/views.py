from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from message.models import List
from message.serializer import ListSerializer


class ClientMessageView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    # def get_queryset(self):
    #     queryset = List.objects.filter()
    #     return 


class UserMessageView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    def get_queryset(self):
        project = self.kwargs.get('message_project')
        return List.objects.filter(sender_id=self.request.user, project_id=project)