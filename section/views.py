from django.http import Http404
from django.db.models import Count, Subquery, OuterRef
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from utils.views import RetrieveUpdateDestroyAPIView
from section.models import List
from section.serializer import Serializer, LinkSerializer, ReadSerializer


class SectionsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ReadSerializer

    def get_queryset(self):
        type = self.kwargs.get("type")

        queryset = self.queryset

        if type == "client":
            queryset = queryset.filter(project__creator=self.request.user.id)
        if type == "user":
            queryset = queryset.filter(user=self.request.user.id)

        suggest_count_subquery = (
            List.objects.values("project_id")
            .annotate(suggest_count=Count("id"))
            .filter(project_id=OuterRef("project_id"))
            .values("suggest_count")[:1]
        )

        queryset = queryset.annotate(suggest_count=Subquery(suggest_count_subquery))

        return queryset


class SectionView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    lookup_field = "id"
    serializer_class = Serializer
    read_serializer_class = LinkSerializer


class SectionsProjectView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        request.data["project"] = self.kwargs.get("project_id")
        return super().create(request, *args, **kwargs)


class SectionProjectView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    lookup_field = "project_id"
    serializer_class = LinkSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(user=self.request.user.id).first()

        if obj is None:
            raise Http404

        return obj
