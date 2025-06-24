from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views import View

from accounts.forms import RegisterUserForm


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
