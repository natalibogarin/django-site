from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo!")

def contact(request):
    return HttpResponse("Hola estoy en la pagina de contacto")