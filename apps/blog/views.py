from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    texto={'mensaje_texto':'Este es mi primer mensaje :)'}
    return render(request, 'index.html',texto)

def contact(request):
    #return HttpResponse("Hola estoy en la pagina de contacto")
    return render(request, 'index copy.html',{})