from django.db import models

from applications.users.models import User
# Create your models here.

class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Horario(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    
    def __str__(self):
        #return self.fecha
        return f"{self.fecha} {self.hora.strftime('%H:%M:%S')}"


class Avion(models.Model):
    identificacion = models.IntegerField(primary_key=True)
    fabricante = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    capacidad_pasajeros = models.IntegerField()
    def __str__(self):
        return self.modelo

class Tarifa(models.Model):
    clase_asiento = models.CharField(max_length=255)
    precio = models.FloatField()

    def __str__(self):
        return self.clase_asiento

class Aerolinea(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Asiento(models.Model):
    clase_asiento = models.CharField(max_length=255)
    fila = models.CharField(max_length=255)
    letra = models.CharField(max_length=255)

class Vuelo(models.Model):
    numero = models.CharField(max_length=255, primary_key=True)
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    aeropuerto_origen = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name='aeropuerto_origen')
    aeropuerto_destino = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name='aeropuerto_destino')
    fecha_llegada = models.ForeignKey(Horario, on_delete=models.CASCADE, related_name='fecha_llegada')
    fecha_salida = models.ForeignKey(Horario, on_delete=models.CASCADE, related_name='fecha_salida')
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE)
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE)
    estado = models.CharField(max_length=255)
    asientos_disponibles = models.IntegerField()
    def __str__(self):
        return self.numero

class Tarjeta(models.Model):
    numero = models.IntegerField(primary_key=True)
    fecha_vencimiento = models.CharField(max_length=5, help_text="Formato: MM/AA")
    nombre = models.CharField(max_length=255)
    empresa_tarjeta = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saldo = models.FloatField(default=7000)
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    codigo_reserva = models.CharField(max_length=255, primary_key=True)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    ESTADO_RESERVA = (
        ('Reservado', 'Reservado'),
        ('Comprado', 'Comprado'),
    )
    estado = models.CharField(max_length=50, choices=ESTADO_RESERVA, default='Reservado')
    def __str__(self):
        return self.codigo_reserva