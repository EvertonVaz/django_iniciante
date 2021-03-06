"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from core.views import *
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/agenda/')),
    path('admin/', admin.site.urls),
    path('evento/<titulo_evento>', dataEvento),
    path('agenda/', lista_eventos),
    path('agenda/historico/', historico),
    path('agenda/lista/<int:id_usuario>', json_lista_evento),
    path('agenda/evento/', evento),
    path('agenda/evento/submit', submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', delete_evento),
    path('login/', login_user),
    path('login/submit', submit_login),
    path('logout/', logout_user)
]
