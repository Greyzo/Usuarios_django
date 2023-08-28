from django.contrib import admin

# Register your models here.
from .models import Aeropuerto, Horario, Avion, Tarifa, Aerolinea, Asiento, Vuelo, Tarjeta, Reserva

# Puedes usar el admin básico para empezar.
admin.site.register(Aeropuerto)
admin.site.register(Horario)
admin.site.register(Avion)
admin.site.register(Tarifa)
admin.site.register(Aerolinea)
admin.site.register(Asiento)
admin.site.register(Vuelo)
admin.site.register(Tarjeta)
admin.site.register(Reserva)