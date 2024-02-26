from django.http import Http404
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from section.models import List
from section.serializer import ListSerializer


class SectionView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = "id"


class ClientSectionView(ListAPIView, UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = "id"
    # def get_queryset(self):
    #     queryset = List.objects.filter()
    #     return


class UserSectionView(RetrieveAPIView, CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = "project_id"

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        project_id = self.kwargs.get("project_id")
        request.data["project"] = project_id
        return super().create(request, *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        fiter = {"user": self.request.user.id}
        obj = queryset.filter(**fiter).first()

        if obj is None:
            raise Http404

        return obj
