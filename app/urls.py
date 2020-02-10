from .views import *
from django.urls import path

urlpatterns = [
    path('reservecar/', reserve_car, name='home'),

    path('reservecar/veiculos', veiculos_page, name='veiculos'),
    path('reservecar/veiculos/cadastrar_veiculos', cadastrar_veiculos, name='cadastrar_veiculos'),
    path('reservecar/veiculos/listar_veiculos', listar_veiculo, name='listar_veiculos'),

    path('reservecar/motorista', motorista_page, name='motorista'),
    path('reservecar/motorista/cadastrar_motorista', cadastrar_motorista, name='cadastrar_motorista'),
    path('reservecar/motorista/listar_motorista', listar_motorista, name='listar_motorista'),

    path('reservecar/reservas', reservas_page, name='reservas'),
    path('reservecar/reservas/cadastrar_reserva', cadastrar_reserva, name='cadastrar_reserva'),
    path('reservecar/reservas/listar_reservas', listar_reservas, name='listar_reservas'),

]
