from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request,"index.html")
def contactos (request):
    return render (request,"contactos.html")
