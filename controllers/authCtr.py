from django.views import View
from django.http import HttpResponse

class authCtr(View):
    def get(self, request):
        return HttpResponse("This is the first view.")