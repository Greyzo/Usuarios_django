from django.urls import path
from . import views

app_name = "intouch_app"

urlpatterns = [
    path('vuelos/', views.listar_vuelos, name='listar_vuelos'),
    path('agregar-tarjeta/', views.agregar_tarjeta, name='agregar_tarjeta'),
    path('comprar-billete/<int:vuelo_id>/', views.comprar_billete, name='comprar_billete'),
    path('reservar/', views.reserva_vuelos, name='reservar_vuelo'),
    path('consulta/', views.consulta_vuelos, name='consulta_vuelos'),
]