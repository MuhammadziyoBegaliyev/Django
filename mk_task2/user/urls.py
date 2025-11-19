from django.urls import path
from .views import user_info_view

urlpatterns = [
    path("<str:name>/<int:year>/", user_info_view, name="Topshiriq 1" )
]