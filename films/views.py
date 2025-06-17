from django.contrib.admindocs.views import ViewIndexView
from django.shortcuts import render
from django.views import View

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')
    def post(self, request):
        return render(request, 'base.html')