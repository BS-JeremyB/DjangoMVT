from django.urls import path
from . import views


urlpatterns = [
    path('liste/', views.liste_film, name='liste'),
    path('contact/', views.contact, name='contact'),
]
 