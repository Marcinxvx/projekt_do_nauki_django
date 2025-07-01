from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

from films.forms import AddDistributorForm

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
def test_add_author_view(authors): # przyjmuje jako argument funkcjie z dekoratorem z pliku conftest.py bez importu
    c = Client()
    url = reverse('add_author')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['authors'].count() == len(authors) # sprawdzamy czy mamy tyle samo autorow w context co w fixture
    for author in authors:                                     # sprawdzamy czy kazdy autor z fikstury znajduje sie w context
        assert author in response.context['authors']

@pytest.mark.django_db
def test_add_distributor_view(): # nie przkazujemy fikstury bo widok korzysta z formularzy
    c = Client()
    url = reverse('add_distributor')
    response = c.get(url)
    assert response.status_code == 200
    form = response.context['form']             # pobiera z kontekstu dane pod nazwa form
    assert isinstance(form, AddDistributorForm) # sprawdzamy czy obiekt 'form' w widoku jest klasy 'AddDistributorForm', czyli czy przekazuje odpowiedni formularz do kontekstu

