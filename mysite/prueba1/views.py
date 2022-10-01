from django.shortcuts import render
from .models import post1
def muestra_datos (request):
    consulta = post1.objects.all()
    lista =[]
    doc=()
    for i in consulta:
        lista.append(i.x3+i.x4)
        doc = i.x3+i.x4


    contexto ={'data':consulta,'sumas':doc}
    return render (request,'prueba1/index.html',contexto)

def ver (request):
    consulta = post1.objects.all()
 