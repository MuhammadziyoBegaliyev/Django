from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

def user_info_view(request, name, year):
    now_year = int(datetime.now().year)
    return HttpResponse(f"{name}, sizning yoshingiz {now_year - year} da .")