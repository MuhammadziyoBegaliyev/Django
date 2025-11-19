from django.urls import path
from .views import HelloView, BaseView

urlpatterns = [
    path("base/", BaseView.as_view(), name="base"),
    path('', HelloView.as_view(), name='hello')
]