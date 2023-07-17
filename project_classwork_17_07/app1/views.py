from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    data = [x for x in range(1, 10)]

    return JsonResponse(data, safe = False)
