from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    titulo = "Este es el sitio de Crucero Uno"

    mensaje = "Nos gusta tocar weas y estamos con ganas d grabaaaaar jeje"

    data = {
        'titulo': titulo,
        'mensaje': mensaje
    }

    return render(request, 'core/inicio.html', data)
def contacto(request):
    ig_link = 'https://www.instagram.com/crucero_uno/'
    yt_link = 'https://youtube.com/@crucerouno?si=xO2bfVoTyZQwy4-I'
    data = {
        'ig': ig_link,
        'yt': yt_link
    }
    return render(request, 'core/contacto.html', data)
def musica(request):
    discos = ["En procesoooo jeje"]
    canciones = [
        {'titulo': 'Pasarela', 'link':'https://www.youtube.com/watch?v=-4wDfm_hJus'},
        {'titulo': 'Astronauta vagabundo', 'link':'https://www.youtube.com/watch?v=6vAhe_5np4Q'}
    ]
    data = {
        'discos': discos,
        'canciones': canciones
    }
    return render(request, 'core/musica.html', data)