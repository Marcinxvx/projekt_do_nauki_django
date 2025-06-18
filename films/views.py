from django.contrib.admindocs.views import ViewIndexView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views import View
from films.models import Author


# Create your views here.

class AddFilmView(View):
    def get(self, request):
        return render(request, 'films/add_film.html')
    def post(self, request):
        return render(request, 'films/add_film.html')

class AddAuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'films/add_author.html', {'authors': authors})
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Author.objects.create(first_name=first_name, last_name=last_name)
        return HttpResponseRedirect(reverse('add_author'))