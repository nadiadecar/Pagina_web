from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'peluqueria/index.html')

def nosotros(request):
    return render(request, 'peluqueria/nosotros.html')

def servicios(request):
    return render(request, 'peluqueria/servicios.html')

def contacto(request):
    return render(request, 'peluqueria/contacto.html')

def reserva(request):
    return render(request, 'peluqueria/reserva.html')


def inventario(request):
    return render(request, 'peluqueria/inventario.html')

def checkfn(request):
	 if request.POST['inputCheck1'] == 'on':
	 	return "Si" 
	 else: return "No"

def add_reserva(request):
	nombre =request.POST['nombre']
	fecha = request.POST['fecha']
	email = request.POST['correo']
	servico = request.POST['servico']
	check = checkfn(request)

	contexto = {"form":"Reserva creada con exito", "gracias":"Muchas gracias",
	"Nombre":nombre, "Fecha":fecha, "Email":email, "Servicios":servicio, "check":check}
	
	return render(request, 'miapp/added_reserva.html', contexto) 
