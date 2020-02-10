from .forms import FormVeiculo, FormMotorista, FormReserva
from django.shortcuts import render
from .models import *
import datetime
import pytz
from django.http import HttpResponseRedirect
# Create your views here.


def reserve_car(request, template_name="base.html"):
    return render(request, template_name)


def veiculos_page(request, template_name="veiculos.html"):
    return render(request, template_name)


def cadastrar_veiculos(request, template_name="cadastrar_veiculos.html"):
    form = FormVeiculo(request.POST, request.FILES)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            template_name = "veiculos.html"
    else:
        form = FormVeiculo()
    return render(request, template_name, context)


def listar_veiculo(request, template_name="listar_veiculos.html"):
    veiculo = Veiculo.objects.all()
    veiculos = {'lista': veiculo}
    return render(request, template_name, veiculos)


def motorista_page(request, template_name="motorista.html"):
    return render(request, template_name)


def cadastrar_motorista(request, template_name="cadastrar_motorista.html"):
    form = FormMotorista(request.POST)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            template_name = "motorista.html"
    else:
        form = FormMotorista
    return render(request, template_name, context)


def listar_motorista(request, template_name="listar_motorista.html"):
    query = request.GET.get("busca", '')
    if query:
        motorista = Motorista.objects.filter(nome__icontains=query)
    else:
        motorista = Motorista.objects.all()
    motorista = {'lista': motorista}
    return render(request, template_name, motorista)


def reservas_page(request, template_name="reservas.html"):
    return render(request, template_name)


def cadastrar_reserva(request, template_name="cadastrar_reserva.html"):
    utc = pytz.UTC
    form = FormReserva(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            reserva = Reserva.objects.all()
            # Captura dados dos forms
            data_inicio = (form.data['data_inicio'])
            data_inicio = data_inicio.replace("T", " ")
            data_final = (form.data['data_final'])
            data_final = data_final.replace("T", " ")
            veiculo_form = (form.data['veiculo'])

            # Converte a string do Form em datetime
            data_final_form = datetime.datetime.strptime(data_final, '%Y-%m-%d %H:%M')
            data_inicio_form = datetime.datetime.strptime(data_inicio, '%Y-%m-%d %H:%M')

            # UTC Local
            data_final_form = pytz.utc.localize(data_final_form)
            data_inicio_form = pytz.utc.localize(data_inicio_form)

            # Capture Veiculo
            veiculo_model = Veiculo.objects.get(pk=veiculo_form)

            # Verificação se já existe uma reserva na data selecionada
            for reserva in reserva:
                if ((data_final_form >= reserva.data_inicio) and (data_final_form <= reserva.data_final) or \
                        (data_inicio_form >= reserva.data_inicio) and (data_inicio_form <= reserva.data_final)):
                    if str(reserva.veiculo.pk) == veiculo_form:
                        if (reserva.estado_reserva == "Confirmado") or (reserva.veiculo.estado == "manutenção"):
                            return render(request, template_name="cadastrar_reserva_erro.html")
                            #return render(request, template_name="cadastrar_reserva_erro2.html")
                    else:
                        if veiculo_model.estado == "manutenção":
                            return render(request, template_name="cadastrar_reserva_erro.html")
                else:
                    if veiculo_model.estado == "manutenção":
                        return render(request, template_name="cadastrar_reserva_erro.html")
            instance = form.save(commit=False)
            instance.estado_reserva = 'Confirmado'
            instance.save()
            template_name = "reservas.html"

    else:
        form = FormReserva
    return render(request, template_name, context)


def listar_reservas(request, template_name="listar_reservas.html"):
    query = request.GET.get("cancelar_reserva", '')
    reserva = Reserva.objects.all()
    if query:
        for reserva in reserva:
            if reserva.pk == int(query):
                reserva.estado_reserva = "Cancelada"
                reserva.save()
                return HttpResponseRedirect('/reservecar/reservas/listar_reservas')
    reservas = Reserva.objects.all()
    reservas = {'lista': reservas}
    return render(request, template_name, reservas)