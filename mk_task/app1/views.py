from django.shortcuts import render, HttpResponse

# Create your views here.


def hello_view(request):
    return HttpResponse("Hello, World!")


def hello_name_view(request, ism ):
    return HttpResponse(f"Hello, {ism}!")


