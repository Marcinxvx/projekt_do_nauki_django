"""
URL configuration for projekt_do_nauki_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from films import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('add_film/', views.AddFilmView.as_view(), name='add_film'),
    path('add_author/', views.AddAuthorView.as_view(), name='add_author'),
    path('delete_author/<int:primary_key>', views.DeleteAuthorView.as_view(), name='delete_author'), # z add_author.html dostaje <a href= z danymi iprzekazuje do adresu i odpala widok, potem wracamy znowu tutaj poprzez delete_author.html bo w formularzu mamy metode POST, dane juz mamy z paska adresu np. /delete_author/5
    path('update_author/<int:primary_key>', views.UpdateAuthorView.as_view(), name='update_author'),
    path('add_publisher/', views.AddPublisherView.as_view(), name='add_publisher'),
    path('delete_publisher/<int:primary_key>', views.DeletePublisherView.as_view(), name='delete_publisher'),
    path('update_publisher/<int:primary_key>', views.UpdatePublisherView.as_view(), name='update_publisher'),
    path('add_distributor/', views.AddDistributorView.as_view(), name='add_distributor'),
    path('add_genre/', views.AddGenreView.as_view(), name='add_genre'),
    path('film_list/', views.FilmListView.as_view(), name='film_list'),
    path('accounts/', include('accounts.urls')), # tworzymy nowy plik urls.py w aplikacji account i tam trzymamy do niej url, aby uniknac powtorzenia importu 'from films import views' zeby nie bylo 2x 'views'
                                                       # bedzie podstawial adresy np 'accounts/register/' czy 'accounts/login/'
                                                       # w tych głównych urls.py mozna zostawic tylko to co powyzej i analogicznie adresy do innych apliakcji np. 'path('films/', include('films.urls'))', ale nie przeklejam zeby sie nie pogubic
                                                       # a wszystkie szeczególowe urlsy np 'add_film/' poprzenosci do aplikacji abby byl porzadek

]
