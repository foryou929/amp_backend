from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from payment.models import List as PaymentList
from section.models import List as SectionList
from payment.serializer import ListSerializer


class PaymentListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        queryset = PaymentList.objects.select_related("section").select_related("section__project")

        if kwargs.get("type") == "client":
            queryset = queryset.filter(section__project__creator=request.user.id)
        if kwargs.get("type") == "user":
            queryset = queryset.filter(section__user=request.user.id)

        serializer = ListSerializer(queryset, many=True)
        return Response(serializer.data)


class SectionPaymentView(CreateAPIView, RetrieveAPIView, UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PaymentList.objects.all()
    serializer_class = ListSerializer
    lookup_field = "section_id"

    def create(self, request, *args, **kwargs):
        request.data["section"] = self.kwargs.get("section_id")
        return super().create(request, *args, **kwargs)
