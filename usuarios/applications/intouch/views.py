from django.shortcuts import render
from .models import * 
from .forms import *
from django.shortcuts import redirect
import uuid

# Create your views here.
def listar_vuelos(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'intouch/vuelos.html', {'vuelos': vuelos})

def reserva_vuelos(request):
    aeropuertos = Aeropuerto.objects.all()  # <-- Define aeropuertos aquí al inicio de la función

    if request.method == "POST":
        origen_id = request.POST.get("origen")
        destino_id = request.POST.get("destino")
        fecha = request.POST.get("fecha")
        vuelos = Vuelo.objects.filter(
            aeropuerto_origen_id=origen_id,
            aeropuerto_destino_id=destino_id,
            fecha_salida__fecha=fecha
        )
        return render(request, 'intouch/Reserva.html', {'aeropuertos': aeropuertos, 'vuelos': vuelos})

    return render(request, 'intouch/Reserva.html', {'aeropuertos': aeropuertos})

def agregar_tarjeta(request):
    if request.method == 'POST':
        form = TarjetaForm(request.POST)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.user = request.user
            tarjeta.save()
            # redirecciona a donde quieras después de guardar la tarjeta
    else:
        form = TarjetaForm()

    return render(request, 'intouch/tarjeta.html', {'form': form})

def comprar_billete(request, vuelo_id):
    vuelo = Vuelo.objects.get(pk=vuelo_id)
    if not request.user.is_authenticated:
        return redirect('login') 
    if vuelo.asientos_disponibles <= 0:
        return render(request, 'intouch/sin_asientos.html')
    try:
        tarjeta = Tarjeta.objects.get(user=request.user)
    except Tarjeta.DoesNotExist:
        return redirect('intouch_app:agregar_tarjeta')
    if tarjeta.saldo < vuelo.tarifa.precio:
        return render(request, 'intouch/saldonot.html')
    if request.method == 'POST':
        tarjeta.saldo -= vuelo.tarifa.precio
        tarjeta.save()
        vuelo.asientos_disponibles -= 1
        vuelo.save()
        codigo_reserva_generado = str(uuid.uuid4())[:8]
        Reserva.objects.create(
            codigo_reserva=codigo_reserva_generado,
            tarjeta=tarjeta,
            vuelo=vuelo,
            estado='Comprado'
        )
        return render(request, 'intouch/exito.html')
    return render(request, 'intouch/billetes.html', {'vuelo': vuelo})



def consulta_vuelos(request):
    tipo_consulta = request.POST.get('tipo_consulta') if request.method == "POST" else None
    consulta_form = None
    vuelos = Vuelo.objects.all()

    FORM_MAPPING = {
        'horarios': (HorariosVuelosForm, ['fecha', 'hora']),
        'tarifas': (TarifasVuelosForm, ['tarifa']),
        'info': (InformacionVueloForm, ['origen', 'destino', 'aerolinea'])
    }

    if tipo_consulta in FORM_MAPPING:
        consulta_form = FORM_MAPPING[tipo_consulta][0](request.POST or None)
        campos_mostrar = FORM_MAPPING[tipo_consulta][1]

        if request.method == "POST" and consulta_form.is_valid():
            vuelos = apply_filters(tipo_consulta, consulta_form, vuelos)

    context = {
        'consulta_form': consulta_form,
        'vuelos': vuelos,
        'form_type': tipo_consulta,
    }
    return render(request, 'intouch/vuelos.html', context)

def apply_filters(tipo_consulta, form, queryset):
    filters = {}
    if tipo_consulta == 'horarios':
        fecha = form.cleaned_data.get('fecha')
        hora = form.cleaned_data.get('hora')
        
        
        if fecha:
            filters['fecha_salida__fecha'] = fecha
        if hora:
            filters['fecha_salida__hora'] = hora

    elif tipo_consulta == 'tarifas':
        tarifa = form.cleaned_data.get('clase_asiento')
        if tarifa:
            filters['tarifa'] = tarifa

    elif tipo_consulta == 'info':
        origen = form.cleaned_data.get('aeropuerto_origen')
        destino = form.cleaned_data.get('aeropuerto_destino')
        aerolinea = form.cleaned_data.get('aerolinea')
        if origen:
            filters['aeropuerto_origen'] = origen
        if destino:
            filters['aeropuerto_destino'] = destino
        if aerolinea:
            filters['aerolinea'] = aerolinea

    return queryset.filter(**filters)