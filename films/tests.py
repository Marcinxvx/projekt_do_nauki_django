from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

from films.forms import AddDistributorForm
from films.models import Author, Distributor, Film

# Create your tests here.

"""
def test_env(): # piszemy zawsze na poczatku aby spraawdzic czy dzialja tesy czy jest konfiguracjia w file po lewej na gorze settings
    assert 1

@pytest.mark.django_db # nastepnie odpalamy test z dekoratorem i sprawcdzamy czy w console logu zrobila sie migracji bazy danych, jezlei tak to dziła
def test_env():
    assert 1
"""
@pytest.mark.django_db
def test_index_view():
    c = Client()
    url = '/'
    response = c.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_author_view_get(authors): # przyjmuje jako argument funkcjie z dekoratorem z pliku conftest.py bez importu
    c = Client()
    url = reverse('add_author')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['authors'].count() == len(authors) # sprawdzamy czy mamy tyle samo autorow w context co w fixture
    for author in authors:                                     # sprawdzamy czy kazdy autor z fikstury znajduje sie w context
        assert author in response.context['authors']

@pytest.mark.django_db
def test_add_distributor_view_get(): # nie przkazujemy fikstury bo widok korzysta z formularzy
    c = Client()
    url = reverse('add_distributor')
    response = c.get(url)
    assert response.status_code == 200
    form = response.context['form']             # pobiera z kontekstu dane pod nazwa form
    assert isinstance(form, AddDistributorForm) # sprawdzamy czy obiekt 'form' w widoku jest klasy 'AddDistributorForm', czyli czy przekazuje odpowiedni formularz do kontekstu

@pytest.mark.django_db
def test_add_author_view_post():
    c = Client()
    url = reverse('add_author')
    data = {
        'first_name': "Adam",
        'last_name': 'Kowalski'
    }
    response = c.post(url, data)
    assert response.status_code == 302
    assert Author.objects.get(**data) # sprawdzamy czy dane sie zapisaly do bazy pobierajac je (rozpakowujemy slownik z danymi)

@pytest.mark.django_db
def test_add_distributor_view_post_is_valid(): # test jezeli w imieniu jest zawarta litera "s" tak jak w walidatorze w models.py
    c = Client()
    url = reverse('add_distributor')
    data ={
        'name': "Darek_sss",
        'year': 2012
    }
    response = c.post(url, data)
    assert response.status_code == 302 # jezeli formularz jest niezwalidowany to wystarczy podstwic '200'
    assert Distributor.objects.get(**data)

@pytest.mark.django_db
def test_add_distributor_view_post_not_valid():  # test jezeli w imieniu jest zawarta litera "s" tak jak w walidatorze w models.py
    c = Client()
    url = reverse('add_distributor')
    data = {
        'name': "Darek",
        'year': 2012
    }
    response = c.post(url, data)
    assert response.status_code == 200  # jezeli formularz jest niezwalidowany to '200' bo w returnie mamy render
    assert not Distributor.objects.exists() # upewniamy sie przy niezwalidowanym formulardzu ze obiek sie nie zapisal do bazy danych, czy jest pusta
    form = response.context['form']
    assert form.errors

@pytest.mark.django_db
def test_film_list_view_without_login(): # test gdy urzytkownik jest niezalogowany czy widok da odpowiedz redirect(pierwszy assert) i czy przekieruje na adres /login (drugi assert)
    c = Client()
    url = reverse('film_list')
    response = c.get(url)
    assert response.status_code == 302 # pomimo że metoda jest get, to widok wymaga aby user byl zalogowany i przekierowuje do widoku logowani czli daje odpowiedz Redirecta wiec odpowiedz 302
    assert response.url.startswith(reverse('login')) # response.url, to adres na ktory zostelismy przekierowani, sprawdzamy czy przekierowuje nas na adres logowania czy string c.get(url) zaczyna sie od /login

@pytest.mark.django_db
def test_film_list_view_login(user, films): # nie musimy przekazywac dodatkowych fixtur, ktore sa w relacji bazodanowej do films bo w fixturze ja dodalismy do fixtury films
    c = Client()
    c.force_login(user) # niepotrzebujemy sprawdzac loginu i hasla, nie potrzebujemy sprawdzac jego prawa do zalogowania, potrebujemy zeby poprostu byl zalogowany, by widok dzialal
    url = reverse('film_list')
    data = {
        'title': 'Film 1' # 'title' to klucz z widoku, 'Film 1' to wartosc ktora wpisuje uzytkownik w formularz wyszukiwania filmu w widoku
    }
    response = c.get(url, data)
    assert response.status_code == 200
    assert response.context['films'].count() == 1 # sprawdzamy ile filmow zostalo znalezionych po przefiltrowaniu, tylko jeden ma name "Film 1"

# test na dodawanie obiektow, ktore zaleza od innych obiektów
@pytest.mark.django_db
def test_add_film_view_post(authors, publishers, genres): # przekazujemy fixtury, ponieważ bedzeimy odwolywac sie do nich w slowniku 'data' ponizej
    c = Client()
    url = reverse('add_film')
    data = {              # symulujemy dane wprowadzane przez urzytkowika do formularza
        'title': 'testowy',
        'author': authors[0].id, # W HTML formularzu, gdy wybieramy autora, to przeglądarka wysyła do Django tylko jego numer id Nie może wysłać całego obiektu autora, ymulujemy to, co robi przeglądarka: wysyła id autora, symulujemy w html np: "value=1, ktore w bazie odpowiada key
        'publisher': publishers[0].id, # to co jest w HTML jako value w <select>, to najczęściej primary key (czyli id) obiektu w bazie danych.
        'genres': [genre.id for genre in genres], # pobiera id z każdego gatunku i Ssmuluje, że w formularzu użytkownik zaznaczył wszystkie dostępne gatunki
    }
    response = c.post(url, data)
    assert response.status_code == 302
    assert Film.objects.get(title='testowy')
"""         !!!!!!!!!     
NIE wpisujemy ID "na sztywno" (np. 'author': 1), tylko pobieramy je dynamicznie (np. 'author': authors[0].id)
W SQLite testowa baza danych jest tworzona od nowa przy każdym teście, więc ID zwykle zaczynają się od 1.
W PostgreSQL testowa baza nie jest tworzona od nowa, tylko czyszczona — ID mogą rosnąć z każdym testem (np. 8, 15, 27...).
Dlatego wpisując ID na sztywno, test może się wywalić, bo taki obiekt może nie istnieć.
ZAWSZE pobieramy ID bezpośrednio z obiektu, np. genre.id albo author.id – wtedy test działa niezależnie od bazy danych.
"""
