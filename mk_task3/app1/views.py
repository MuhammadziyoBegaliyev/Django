from django.shortcuts import render
from random import randint
from django.views.generic import TemplateView

# Create your views here.

class HelloView(TemplateView):
    template_name = "app1/hello.html"


class BaseView(TemplateView):
    template_name = "app1/base.html"