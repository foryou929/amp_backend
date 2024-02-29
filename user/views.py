from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from user.models import List
from user.serializer import ProfileSerializer


# Create your views here.
class UsersView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)


class UserView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    lookup_field = "id"
    serializer_class = ProfileSerializer
