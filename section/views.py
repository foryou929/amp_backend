from django.http import Http404
from django.db.models import Count, Subquery, OuterRef
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from utils.views import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from section.models import List
from section.serializer import ReadSerializer, Serializer


class SectionListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = Serializer
    read_serializer_class = ReadSerializer

    def get_queryset(self):
        suggest_count_subquery = (
            List.objects.values("project_id")
            .annotate(suggest_count=Count("id"))
            .filter(project_id=OuterRef("project_id"))
            .values("suggest_count")[:1]
        )

        queryset = List.objects.filter(
            project__creator=self.request.user.id,
            step__gte=self.kwargs.get("step_from"),
            step__lte=self.kwargs.get("step_to"),
        ).annotate(suggest_count=Subquery(suggest_count_subquery))

        return queryset


class SectionView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    lookup_field = "id"
    serializer_class = Serializer
    read_serializer_class = ReadSerializer


# class ClientSectionView(ListAPIView, UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = List.objects.all()
#     serializer_class = ListSerializer
#     lookup_field = "id"
# def get_queryset(self):
#     queryset = List.objects.filter()
#     return


class SectionProjectView(CreateAPIView, RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        request.data["project"] = self.kwargs.get("project_id")
        return super().create(request, *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(user=self.request.user.id).first()

        if obj is None:
            raise Http404

        return obj
