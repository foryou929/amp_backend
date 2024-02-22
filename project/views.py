from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from project.models import List
from project.serializer import ListSerializer
from rest_framework.response import Response


# Create your views here.
class ProjectView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def create(self, request, *args, **kwargs):
        # Add foreign key values to request data
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)

    def get(self, request):
        recruiting = ListSerializer(
            List.objects.filter(user_id=request.user.id, progress=1), many=True
        )
        progressing = ListSerializer(
            List.objects.filter(
                user_id=request.user.id, progress__gt=1, progress__lt=11
            ),
            many=True,
        )
        completed = ListSerializer(
            List.objects.filter(user_id=request.user.id, progress=11), many=True
        )
        return Response(
            {
                "recruiting": recruiting.data,
                "progressing": progressing.data,
                "finish": completed.data,
            }
        )
