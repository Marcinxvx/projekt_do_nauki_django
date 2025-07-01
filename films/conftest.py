import pytest
from films.models import Author, Distributor


@pytest.fixture
def authors():
    lst = []
    for i in range(5):
        lst.append(Author.objects.create(first_name=f"Name {i}", last_name=f"Surname {i}"))
    return lst

@pytest.fixture
def distributors():
    lst = []
    for i in range(5):
        lst.append(Distributor.objects.create(name=f"Name {i}", year=i + 2000))
    return lst