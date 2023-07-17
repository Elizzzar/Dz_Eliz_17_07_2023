from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    data = [x for x in range(1, 10)]

    return HttpResponse(data, safe = False)