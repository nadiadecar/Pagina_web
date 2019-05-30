from django.db import models

# Create your models here.
    
class Servicios(models.Model):
    nombre_servicio = models.CharField(max_length=256)
    precio = models.IntegerField(45)
    espacio_fisico = models.CharField(max_length=256)
    tiempo_de_duracion = models.IntegerField(45)
    

class Inventario(models.Model):
	nombre_producto = models.CharField(max_length=100)
	cantidad_producto = models.IntegerField(45)
	marca_producto = models.CharField(max_length=100)
	

class Trabajadores(models.Model):
	nombre_completo = models.CharField(max_length=256)
	rut = models.CharField(max_length=45)
	telefono = models.IntegerField(45)
	correo = models.CharField(max_length=256)
	direccion = models.CharField(max_length=256)
	funcion = models.CharField(max_length=45)
	
	
class Clientes(models.Model):
    nombre_completo = models.CharField(max_length=256)
    rut = models.CharField(max_length=45)
    telefono = models.IntegerField(45)
    correo = models.CharField(max_length=256)
    Trabajadores = models.ForeignKey(Trabajadores, on_delete=models.CASCADE)


class Reservas(models.Model):
	Clientes = models.ForeignKey(Clientes , on_delete=models.CASCADE)
	dia = models.IntegerField(45)
	mes = models.IntegerField(45)
	ano = models.IntegerField(45)
	Hora = models.IntegerField(45)


class Trabajadores_has_Servicios(models.Model):
	servicios=models.ForeignKey(Servicios,on_delete=models.CASCADE)
	trabajadores=models.ForeignKey(Trabajadores, on_delete=models.CASCADE)



class Servicios_has_Inventario(models.Model):
	servicios=models.ForeignKey(Servicios,on_delete=models.CASCADE)
	inventario=models.ForeignKey(Inventario, on_delete=models.CASCADE)




