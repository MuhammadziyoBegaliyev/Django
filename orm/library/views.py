from django.shortcuts import render, redirect
from .models import Kitob
from .forms import KitobForm

# Create your views here.


def books_list_view(request):
    if request.method == "POST":
        form =KitobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books list")
    books = Kitob.objects.all()
    form = KitobForm()
    return render(request, "library/books.html", {"books": books, "form": form})



def del_kitob_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    kitob.delete()
    return redirect("books list")

def edit_kitob_view(request, kitob_id):
    if request.method == "Post":
        kitob = Kitob.objects.get(id=kitob_id)
        form = KitobForm(request.POST, instance=kitob)
        if form.is_valid():
            form.save()
    kitob = Kitob.objects.get(id=kitob_id)
    books = Kitob.objects.all()
    form = KitobForm(instance=kitob)
    return render(request, "library/books.html", {"books": books, "form": form})