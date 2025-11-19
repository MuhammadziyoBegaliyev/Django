from django.shortcuts import render, HttpResponse
from calendar import HTMLCalendar

# Create your views here.

def calendar_view(request, year, month):
    cal = HTMLCalendar()
    cal = cal.formatmonth(year, month)
    return HttpResponse(f"<center>{cal}</center>")