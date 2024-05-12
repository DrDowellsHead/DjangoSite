from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def advantages(request):
    return render(request, 'main/advantages.html')


def photos(request):
    return render(request, 'main/photos.html')


def authorization(request):
    return render(request, 'main/authorization.html')
