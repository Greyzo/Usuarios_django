from django import forms
from .models import *

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['numero', 'fecha_vencimiento', 'nombre', 'empresa_tarjeta']



class ConsultaVuelosForm(forms.Form):
    TIPO_CONSULTA_CHOICES = (
        ('horarios', 'Horarios de Vuelos'),
        ('tarifas', 'Tarifas de Vuelos'),
        ('info', 'Información de Vuelo'),
    )
    tipo_consulta = forms.ChoiceField(choices=TIPO_CONSULTA_CHOICES, required=True, widget=forms.RadioSelect, initial='horarios')
    origen = forms.ModelChoiceField(queryset=Aeropuerto.objects.all(), required=True)
    destino = forms.ModelChoiceField(queryset=Aeropuerto.objects.all(), required=True)
    fecha = forms.DateField(widget=forms.SelectDateWidget(), required=True)
    hora = forms.TimeField(required=False) 
    aerolinea = forms.ModelChoiceField(queryset=Aerolinea.objects.all(), required=False)
    
    # Agregamos el campo de tarifa
    tarifa = forms.ModelChoiceField(queryset=Tarifa.objects.all(), required=False, label="Tarifa")


class HorariosVuelosForm(forms.Form):
    fecha = forms.DateField(widget=forms.SelectDateWidget(), required=True)
    hora = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), required=True)

class TarifasVuelosForm(forms.Form):
    clase_asiento = forms.ModelChoiceField(queryset=Tarifa.objects.all(), required=True)

class InformacionVueloForm(forms.Form):
    aeropuerto_origen = forms.ModelChoiceField(queryset=Aeropuerto.objects.all(), required=True, label='Origen')
    aeropuerto_destino = forms.ModelChoiceField(queryset=Aeropuerto.objects.all(), required=True, label='Destino')
    aerolinea = forms.ModelChoiceField(queryset=Aerolinea.objects.all(), required=True)