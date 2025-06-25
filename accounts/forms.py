from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput()) # sztucznie generujemy haslo, nie poslugujemy sie haslem z modelu User, aby moc cos z nim zrobi w kalsie potem
    password2 = forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        data = super().clean() # tworzymy swoja funkcjie clean ale wywolujemy na bazowej funkcji django czyli .clean()  ,zmienna data jest slownikiem, uruchami sie gdy w widoku robimy .is_valid i ma dostep do danych z formularza
        if data['password1'] != data['password2']:  # czli do metody django .clean dodajemy naszego 'if' oraz 'raise poprzez 'super()'
            raise forms.ValidationError("Passwords mismatch")
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"})) #nie łaczymy w jeden form z Register, tworzymy osobno zgodnie ze sztuka
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))