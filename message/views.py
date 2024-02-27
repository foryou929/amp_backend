from django.http import Http404
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from message.models import List
from message.serializer import ListSerializer


class MessageView(CreateAPIView, RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = "section_id"

    def create(self, request, *args, **kwargs):
        request.data["sender"] = request.user.id
        request.data["section"] = self.kwargs.get("section_id")
        return super().create(request, *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(type=step.kwargs.get("step")).first()

        if obj is None:
            raise Http404

        return obj


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
