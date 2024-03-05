from django.http import Http404
from django.db.models import Count, Subquery, OuterRef
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from utils.views import RetrieveUpdateDestroyAPIView
from section.models import List
from section.serializer import Serializer, LinkSerializer, SectionListSerializer


class SectionsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        queryset = List.objects.all()

        if kwargs.get("type") == "client":
            queryset = queryset.filter(project__creator=request.user.id)
        if kwargs.get("type") == "user":
            queryset = queryset.filter(user=request.user.id)

        suggest_count_subquery = (
            List.objects.values("project_id")
            .annotate(suggest_count=Count("id"))
            .filter(project_id=OuterRef("project_id"))
            .values("suggest_count")[:1]
        )

        queryset = queryset.annotate(suggest_count=Subquery(suggest_count_subquery))

        serializer = SectionListSerializer(queryset, many=True)
        return Response(serializer.data)


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


class SectionsProjectView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = request.user.id
        data["project"] = kwargs.get("project_id")
        serializer = Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        object = List.objects.filter(project_id=kwargs.get("project_id")).first()
        if object is None:
            raise Http404
        serializer = LinkSerializer(object)
        return Response(serializer.data)
