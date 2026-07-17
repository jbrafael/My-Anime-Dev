from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_animes, name='lista_animes'),
    path('buscar/', views.buscar_api, name='buscar_api'),
    path('adicionar/', views.adicionar_anime, name='adicionar_anime'),
    path('editar/<int:id>/', views.editar_anime, name='editar_anime'),
    path('excluir/<int:id>/', views.excluir_anime, name='excluir_anime'),
]