from django.urls import path
from .views import books_list_view , del_kitob_view, edit_kitob_view

urlpatterns = [
    path("", books_list_view, name="books list") ,
    path("edit/<int:kitob_id>", edit_kitob_view, name="kitob edit")  ,
    path("del/<int:kitob_id>", del_kitob_view, name="kitob del")
]