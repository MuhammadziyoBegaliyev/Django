from django.urls import path
from .views import hello_view, hello_name_view

urlpatterns = [
    path("hello/<str:ism>", hello_name_view, name="hello name"),
    path("hello/", hello_view, name="hello")
]