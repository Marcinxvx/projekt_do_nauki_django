import pytest
from django.contrib.auth.models import User

from films.models import Author, Distributor, Film, Genre, Publisher


@pytest.fixture
def authors():
    lst = []
    for i in range(5):
        lst.append(Author.objects.create(first_name=f"Name {i}", last_name=f"Surname {i}"))
    return lst

@pytest.fixture
def publishers():
    lst = []
    for i in range(5):
        lst.append(Publisher.objects.create(name=f"Publisher {i}", year=i+2000))
    return lst

@pytest.fixture
def genres():
    lst = []
    for i in range(5):
        lst.append(Genre.objects.create(name=f"Genre {i}"))
    return lst

@pytest.fixture
def user():
    return User.objects.create_user(username="testowy", password="ala ma kota") # możemy uzyc genrealnej metody .create , ale dzieki metodzie .create_user mamy odrazu zahaszowane haslo

@pytest.fixture
def films(authors, publishers, genres): # przekazujemy wczesniejsze fikstury powyżej, gdyż films ma relacjie z innymi modelami, i mozemy przekazac kolejne pola wymagane z poprzednich fikstur szybciej
    lst = []
    for i in range(5):
        film = Film.objects.create(title=f'Film {i}', author=authors[i],
                            publisher=publishers[i])
        film.genres.add(genres[i]) # musimy dodać genres osobno w przeciwienstwie do authors i distributors, gdyz jest to relacjia many to many fields -
        lst.append(film)           # genres NIE JEST kolumna w tabeli Film, Django tworzy osobną ukrytą tabelę pośrednią, aby ta tabela mogła dostać film_id, najpierw musimy utworzyć Film i zapisać go w bazie (czyli musi mieć ID)
    return lst                     # nie można tworzyc obiektu genres w tym samym momencie co film, poniewz, obiekt film nie ma jeszcze id potrzebnego do tabeli posredniej, wiec genres musimy stworzyc po film, nie wczesniej

