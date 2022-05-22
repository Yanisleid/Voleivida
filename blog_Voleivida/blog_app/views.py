from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'blog_app/home.html')

def historia(request):
    return render(request, 'blog_app/historia.html')

def regras(request):
    return render(request, 'blog_app/regras.html')

def saude(request):
    return render(request, 'blog_app/saude.html')

def sobre(request):
    return render(request, 'blog_app/sobre.html')
