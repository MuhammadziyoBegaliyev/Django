from django.shortcuts import render, HttpResponse
from random import randint

# Create your views here.


def random_range_view(request, a, b):
    son = randint(a, b)
    return HttpResponse(f"<b>Tasadifiy son: </b>{son}")