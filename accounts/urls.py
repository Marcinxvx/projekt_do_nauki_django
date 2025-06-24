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

from django.urls import path
from accounts import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'), # tu mamy url do tej konkretnej apku a w glownych urls.py mamy importowny include i on bedzei podstawial tam adresy np 'accounts/register/' czy 'accounts/login/'
]
