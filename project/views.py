from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from project.models import List
from project.serializer import ListSerializer


class ProjectView(ListCreateAPIView):
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
        queryset = List.objects.filter(user_id=self.request.user.id)
        return queryset


class UserProjectView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = "id"
