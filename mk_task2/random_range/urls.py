from django.urls import path
from .views import random_range_view


urlpatterns = [
    path("<int:a>/<int:b>", random_range_view, name="Topshiriq 2")
]