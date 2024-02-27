from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from payment.models import List
from payment.serializer import ListSerializer


# Create your views here.
class PaymentView(CreateAPIView, RetrieveAPIView, UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = "section_id"

    def create(self, request, *args, **kwargs):
        request.data["section"] = self.kwargs.get("section_id")
        return super().create(request, *args, **kwargs)
