from django.shortcuts import render
from .models import SliderPhoto


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def advantages(request):
    return render(request, 'main/advantages.html')


def photos(request):
    photos = SliderPhoto.objects.all()
    return render(request, 'main/photos.html', {'photos': photos})


def authorization(request):
    return render(request, 'main/authorization.html')
