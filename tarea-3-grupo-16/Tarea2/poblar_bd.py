from peluqueria.models import Servicios, Inventario, Trabajadores, Clientes, Reservas

servicio1=Servicios(nombre_servicio="Pedicure", precio = 5000 , espacio_fisico = "estacion_5 ", tiempo_de_duracion = 20 )
servicio1.save()

servicio2=Servicios(nombre_servicio="Manicure", precio = 10500 , espacio_fisico = "estacion_8" , tiempo_de_duracion = 20)
servicio2.save()

servicio3=Servicios(nombre_servicio="corte_de_pelo", precio = 8000 , espacio_fisico = "esatcion_2", tiempo_de_duracion = 15)
servicio3.save()

servicio4=Servicios(nombre_servicio="Masaje_capilar", precio = 15000 , espacio_fisico = "estacion_6" , tiempo_de_duracion = 30)
servicio4.save()

servicio5=Servicios(nombre_servicio="Tintura", precio = 12000 , espacio_fisico ="estacion_4" , tiempo_de_duracion = 50 )
servicio5.save()

servicio6=Servicios(nombre_servicio="Barberia", precio = 8000 , espacio_fisico = "estacion_3" , tiempo_de_duracion = 15 )
servicio6.save()

servicio7=Servicios(nombre_servicio="Peinados", precio = 15000 , espacio_fisico = "estacion_2" , tiempo_de_duracion =60  )
servicio7.save()

servicio8=Servicios(nombre_servicio="Depilacion_pierna_entera", precio = 10000 , espacio_fisico = "estacion_1", tiempo_de_duracion = 20)
servicio8.save()

servicio9=Servicios(nombre_servicio="Encrespado_de_pestañas", precio = 9000 , espacio_fisico = "estacion_1" , tiempo_de_duracion = 45 )
servicio9.save()

servicio10=Servicios(nombre_servicio="Manicure_express", precio = 5000 , espacio_fisico = "estacion_5", tiempo_de_duracion = 10)
servicio10.save()




Inventario1=Inventario(nombre_producto= "algodon", cantidad_producto= 8, marca_producto = "Eurostil")
Inventario1.save()

Inventario2=Inventario(nombre_producto= "esmalte rojo ", cantidad_producto= 3, marca_producto = "OPI")
Inventario2.save()

Inventario3=Inventario(nombre_producto= "esmalte negro", cantidad_producto= 5, marca_producto = "OPI")
Inventario3.save()

Inventario4=Inventario(nombre_producto= "esmalte transparente", cantidad_producto= 4, marca_producto = "essie")
Inventario4.save()

Inventario5=Inventario(nombre_producto= "shampoo", cantidad_producto= 5, marca_producto = "Kerastase")
Inventario5.save()

Inventario6=Inventario(nombre_producto= "acondicionador", cantidad_producto= 5, marca_producto = "loreal")
Inventario6.save()

Inventario7=Inventario(nombre_producto= "laca", cantidad_producto= 4, marca_producto = "DUO")
Inventario7.save()

Inventario8=Inventario(nombre_producto= "aceite de argan", cantidad_producto= 2, marca_producto = "babyliss")
Inventario8.save()

Inventario9=Inventario(nombre_producto= "mascarilla para el pelo", cantidad_producto= 2, marca_producto = "Imagea")
Inventario9.save()

Inventario10=Inventario(nombre_producto= "decolorante ", cantidad_producto= 6, marca_producto = "Olaplex")
Inventario10.save()




trabajador1=Trabajadores(nombre_completo="Gonzalo Campos", rut="17837654-k", telefono= 959041922, correo= "gnzl.cmps@live.cl", direccion ="Pasaje el tabo 1338", funcion="Peluquero")
trabajador1.save()

trabajador2=Trabajadores(nombre_completo="Julio Perez", rut="18654231-5", telefono= 950267099, correo= "Jupop.070@icloud.com", direccion ="Pasaje Miraflores 1256", funcion="Peluquero")
trabajador2.save()

trabajador3=Trabajadores(nombre_completo="Patricio Flores",rut="18543123-8", telefono= 950266549, correo= "Patricio.flores@gmail.com", direccion ="Pasaje Miraflores 1256", funcion="Barbero")
trabajador3.save()     
                    
trabajador4=Trabajadores(nombre_completo="Pamela Carrasco",rut="17777564-9", telefono= 826267098, correo= "Pamecarrasco.@gmail.com", direccion ="Pasaje Miraflores 1256", funcion="Manicurista/Pedicurista")
trabajador4.save()
                                        





Cliente=Clientes(nombre_completo="Juan Perez", rut="19837783-1", telefono=123456789, correo="juanperez@gmail.com", Trabajadores= trabajador1)
Cliente.save()

Cliente1=Clientes(nombre_completo="Francisca Santa Cruz", rut="10386365-2", telefono=971373183, correo="franciscast@gmail.com", Trabajadores= trabajador2)
Cliente1.save()

Cliente2=Clientes(nombre_completo="Nadia Silva", rut="124592390-4", telefono=987654321, correo="nadiasilva@gmail.com", Trabajadores= trabajador1)
Cliente2.save()

Cliente3=Clientes(nombre_completo="Mariano Suarez", rut="13246080-5", telefono=987655521, correo="marianosuarez@gmail.com", Trabajadores= trabajador3)
Cliente3.save()

Cliente4=Clientes(nombre_completo="Valentina Alvear", rut="9999486-2", telefono=989954321, correo="valentinalvear@gmail.com", Trabajadores= trabajador3)
Cliente4.save()

Cliente5=Clientes(nombre_completo="Pedro Torres", rut="18453647-7", telefono=987654333, correo="pedrotorres@gmail.com", Trabajadores= trabajador1)
Cliente5.save()

Cliente6=Clientes(nombre_completo="Camila Castillo", rut="19456347-8", telefono=987654358, correo="camilacastillo@gmail.com", Trabajadores= trabajador4)
Cliente6.save()


Cliente7=Clientes(nombre_completo="Patricio Perez", rut="15456579-k", telefono=988754090, correo="petricioperez@gmail.com", Trabajadores= trabajador1)
Cliente7.save()


Cliente8=Clientes(nombre_completo="Fernanda Villanueva", rut="19666347-5", telefono=987754150, correo="fernandavillanueva@gmail.com", Trabajadores= trabajador1)
Cliente8.save()


Cliente9=Clientes(nombre_completo="Constanza Martinez", rut="12546373-1", telefono=997601121, correo="constanzamartinez@gmail.com", Trabajadores= trabajador1)
Cliente9.save()




