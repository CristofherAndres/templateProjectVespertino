from django.shortcuts import render

# Create your views here.
def primerTemplate(request):
    return render(request,'primeraApp/primerTemplate.html')

def infoUsuario(request):
    data = {
        'nombre':       'Bruce',
        'apellido':     'Wayne',
        'direccion':    'Ciudad Gotica',
        'correo':       'bruce.wayne@batman.cl',
        'edad':         40
    }
    return render(request,'primeraApp/segundoTemplate.html',data)