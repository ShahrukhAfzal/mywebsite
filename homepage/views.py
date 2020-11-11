from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>Shahrukh Afzal</h1>")
    return render(request, 'index.html')
