from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from space.models import List
from space.serializer import ListSerializer


# Create your views here.
class SpaceView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def create(self, request, *args, **kwargs):
        # Add foreign key values to request data
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)
