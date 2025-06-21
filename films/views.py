from django.contrib.admindocs.views import ViewIndexView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views import View
from films.models import Author, Publisher, Distributor
from films.forms import AddDistributorForm


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

class DeleteAuthorView(View): # widok zostaje uruchomiony z urls.py i z adresu delete_author/<int:primary_key> pobiera primary_key ktore dostal z add_author.html
    def get(self, request, primary_key): #uruchamia sie to bo po wejsciu w link n urls.py jest rzadanie GET'em wyslane
        author = Author.objects.get(pk=primary_key) # ma dane autora z primary_key z bazy tutaj z modeli
        return render(request, 'films/delete_author.html', {'author': author}) # przekazuje obiekt z bazy danych do delete_author.html i renderuje go
    def post(self, request, primary_key): # ponownie z urls.py wracamy do funkcji, dane czyli argument primary_key mamy z paska adresu strony na która weszlismy wczesniej metoda GET np /delete_author/5, poprostu do path jest przekazywana zamiast delete_author/<int:primary_key>, a ta funkcjia jest uruchamiana bo w delete_author.html mam w formularzu napisana metode POST
        if request.POST['operation'] == "Tak":
            author = Author.objects.get(pk=primary_key)
            author.delete()
        return HttpResponseRedirect(reverse('add_author'))

class UpdateAuthorView(View):
    def get(self, request, primary_key):
        author = Author.objects.get(pk=primary_key)
        return render(request, 'films/update_author.html', {'author': author})
    def post(self, request, primary_key):
        author = Author.objects.get(pk=primary_key)
        author.first_name = request.POST['first_name']
        author.last_name = request.POST['last_name']
        author.save()
        return HttpResponseRedirect(reverse('update_author', kwargs={'primary_key': primary_key})) # lub args=[primary_key], musmy przekazac odnosnik do urls.py bo path tego wymaga update_author/<int:primary_key>
                                                                                                            # args = [...] — lista pozycyjna ---> Musi się zgadzać kolejność z tym, co masz w path():
                                                                                                            # kwargs = {...} — słownik nazwanych argumentów ---> Kolejność nie ma znaczenia
                                                                                                            #                                               ---> Klucze muszą dokładnie pasować do nazw w URL (np. primary_key)
class AddPublisherView(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        return render(request, 'publisher/add_publisher.html', {'publishers': publishers})
    def post(self, request):
        name = request.POST['name']
        year = request.POST['year']
        Publisher.objects.create(name=name, year=year)
        return HttpResponseRedirect(reverse('add_publisher'))

class DeletePublisherView(View):
    def get(selfself, request, primary_key):
        publisher = Publisher.objects.get(pk=primary_key)
        return render(request, 'publisher/delete_publisher.html', {'publsher': publisher})
    def post(self, request, primary_key):
        publisher = Publisher.objects.get(pk=primary_key)
        if request.POST['operation'] == "Tak":
            publisher.delete()
        return HttpResponseRedirect(reverse('add_publisher'))

class UpdatePublisherView(View):
    def get(self, request, primary_key):
        publisher = Publisher.objects.get(pk=primary_key)
        return render(request, 'publisher/update_publisher.html', {'publisher': publisher})
    def post(self, request, primary_key):
        publisher = Publisher.objects.get(pk=primary_key)
        publisher.name = request.POST['name']
        publisher.year = request.POST['year']
        publisher.save()
        return HttpResponseRedirect(reverse('update_publisher', kwargs={'primary_key': primary_key}))

# tworzenie widoków i formularzy na podstawie forms.py -
# sluzy do walidacji danych i tworzenia formularzy, ale itak MUSZE pobrac dane z bazy jeżęli chce je do kontekstu przekazac np. lista dystrybutorow
class AddDistributorView(View):
    def get(self, request):
        distributors = Distributor.objects.all()
        form = AddDistributorForm()
        return render(request, 'distributor/add_distributor.html', {'form': form, 'distributors': distributors} )
    def post(self, request):
        distributors = Distributor.objects.all()
        form = AddDistributorForm(request.POST) # pobieramy formularz wypelniony danymi
        if form.is_valid():                     # walidujemy go wedlug wlasnych standardow z klasy z forms.py
            name = form.cleaned_data['name']    # pobieramy dane z pól
            year = form.cleaned_data['year']    # pobieramy dane z pól
            Distributor.objects.create(name=name, year=year) # tworzymy obiek w bazie danych
            return HttpResponseRedirect(reverse('add_distributor'))
        return render(request, 'distributor/add_distributor.html', {'form': form, 'distributors': distributors})

