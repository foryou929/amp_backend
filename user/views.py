from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from user.models import Profile
from user.serializer import ProfileSerializer


# Create your views here.
class ProfileView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        # Add foreign key values to request data
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)
