from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateAPIView(ListCreateAPIView):
    read_serializer_class = None

    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.read_serializer_class
        else:
            return self.serializer_class


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    read_serializer_class = None

    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.read_serializer_class
        else:
            return self.serializer_class
