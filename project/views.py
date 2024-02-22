from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.serializers import ListSerializer
from rest_framework.permissions import IsAuthenticated
from project.models import List


class ProjectView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def create(self, request, *args, **kwargs):
        # Add foreign key values to request data
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)


class ClientProjectView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user_id=self.request.user.id)
        return queryset


class UserProjectView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user_id=self.request.user.id)
        return queryset
