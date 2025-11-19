from django.urls import path
from .views import calendar_view

urlpatterns = [
    path("<int:year>/<int:month>", calendar_view, name="Topshiriq 3")
]