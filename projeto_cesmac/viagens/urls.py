from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),  
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('criar-viagem/', views.criar_viagem, name='criar_viagem'),
    path('viagens/', views.listar_viagens, name='listar_viagens'),
    path('viagem/<int:viagem_id>/', views.detalhar_viagem, name='detalhar_viagem'),
    path('viagem/<int:viagem_id>/reservar/', views.reservar_viagem, name='reservar_viagem'),
]
