from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from utils.views import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from project.models import List
from project.serializer import Serializer, ReadSerializer


class ProjectsView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.annotate(suggest_count=Count("project_sections__id"))
    serializer_class = Serializer
    read_serializer_class = ReadSerializer

    def create(self, request, *args, **kwargs):
        request.data["creator"] = request.user.id
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        if self.kwargs.get("type") == "client":
            return self.queryset.filter(creator=self.request.user.id)
        if self.kwargs.get("type") == "user":
            return self.queryset.filter(project_sections__user=self.request.user.id)
        return self.queryset.filter(status=0)


class ProjectView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.annotate(suggest_count=Count("project_sections__id"))
    lookup_field = "id"
    serializer_class = Serializer
    read_serializer_class = ReadSerializer
