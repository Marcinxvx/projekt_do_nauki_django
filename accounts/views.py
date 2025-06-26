from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views import View

from accounts.forms import RegisterUserForm, LoginForm


# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'distributor/distributor_form.html', {'form': form})
    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # tworzy obiekt, model urzytkownika, ale NIE zapisuje go do bazy danych dzieki commit=False
            user.set_password(form.cleaned_data['password1']) # zaszyfrowuje haslo, ustawia to z formularza
            form.save() # zapisujemy do bazy danych automatycznie stworzonej przez django 'auth_user'
            return HttpResponseRedirect(reverse('home'))
        return render(request, 'distributor/distributor_form.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'distributor/distributor_form.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) # to jest wlasnie "autentykacja", potwierdzamy torzsamość sprawdzmy czy login odpowiada haslu zaszyfrowanemu
            if user is not None:                                      # jak sie zgadza logujemy sie dosystemu
                login(request, user)
                next_url = request.GET.get('next', 'home') # dzieki temu gdy widok class FilmListView(LoginRequiredMixin,View):, przekieruje nas na logowanie bo jest dostepny tylko dla zalogowanych, to po zalogowaniu przekieruje nas odrazu na widok class FilmListView(LoginRequiredMixin,View):
                return HttpResponseRedirect(next_url) # nie musimy przekazywac dodatkowego contex do szablonu, zeby miec dostep do danych urzytkownika bo robi to domyslnie login(request, user)
        return render(request, 'distributor/distributor_form.html', {'form': form, 'error': 'Nie prawidlowe dane logowania'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))