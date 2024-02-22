from django.views import View
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from project.models import List
from project.serializer import ListSerializer
from rest_framework.response import Response


class ClientProjectView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def create(self, request, *args, **kwargs):
        # Add foreign key values to request data
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)

    def get(self, request):
        queryset = List.objects.filter(user_id=request.user.id)
        serializer = ListSerializer(queryset, many=True)
        return Response(serializer)


class UserProjectView(View):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get(self, request):
        queryset = List.objects.filter(user_id=request.user.id)
        serializer = ListSerializer(queryset, many=True)
        return Response(serializer)
