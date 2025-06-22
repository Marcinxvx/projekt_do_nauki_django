from django import forms

from films.models import Film, Genre

def check_name(value):
    if not 's' in value:
        raise forms.ValidationError('Name must have at least one letter s')

class AddDistributorForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nazwa', validators=[check_name]) # mozemy wiele walidatorow, dac bo to lista, mozna to lub w innym pliku validatory pisac
    year = forms.IntegerField(label='Rok')

class AddFilmForm(forms.ModelForm): # Formularz Modelowy
    class Meta:                     # meta dane klasy (czyli dane opisujace dane, np kiedy zdjiecie zostalo zrobione, gdzie itd)
        model = Film                # odnosi sie do modelu Film
        fields = "__all__"          # dziedziczy jego wszystkie pola
        widgets = {
            'genres': forms.CheckboxSelectMultiple, # podajemy nazwe pola z Modelu czyli np: genres = models.ManyToManyField(Genre)
        }

class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"

class FilmSearchForm(forms.Form):
    title = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))# zmieniamy widget tylko dal tego konkretnego elementu title
