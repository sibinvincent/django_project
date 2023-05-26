from django.http import HttpResponse
from django.shortcuts import render
from .models import Product



# Create your views here.


def index(request):
    return HttpResponse("Hello this is my index page")


def test_fun(request):
    return render(request, 'test.html')


def hom_fun(request):
    return render(request, 'hom.html')
