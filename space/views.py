from utils.views import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from space.models import List
from space.serializer import Serializer, ReadSerializer


# Create your views here.
class SpacesView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = Serializer
    read_serializer_class = ReadSerializer

    def create(self, request, *args, **kwargs):
        request.data["creator"] = request.user.id
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get("type") == "user":
            queryset = queryset.filter(creator=self.request.user.id)
        return queryset


class SpaceView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = Serializer
    read_serializer_class = ReadSerializer
    lookup_field = "id"
