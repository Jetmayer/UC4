from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def saludo(request):
    return render(request,'saludo.html')

def numeros(request):
    return render(request,'numeros.html') 

        
def numeros2(request):
    return render(request,'numeros2.html')    








