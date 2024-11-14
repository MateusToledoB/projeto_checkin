from django.shortcuts import render
from .models import Evento

def ver_eventos(request):
    
    eventos = Evento.objects.all()
    return render(request, 'eventos/ver_eventos.html', {'eventos': eventos})
