from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Album
from .forms import AlbumForm
from .forms import PhotoForm
from .models import Photo

def index(request):
    albums = Album.objects.filter(user_id=request.user.id)
    return render(request, "index.html", {"albums": albums})


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/registration.html", {"form": form})

@login_required
def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.INFO, "Album bylo přidáno.")
            return redirect("index")
    else:
        form = AlbumForm()
    return render(request, "add_album.html", {"form": form})

@login_required
def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id, user_id=request.user.id)
    if request.GET.get("search"):
        photos=album.photo_set.filter(name__icontains=request.GET.get("search"))
    else:
        photos=album.photo_set.all()
    return render(request,"detail.html",{"album": album,"photos":photos})

@login_required
def add_foto(request, album_id):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.album_id = album_id
            instance.save()
            messages.add_message(request, messages.INFO, "Fotka byla přidána")
            return redirect("detail", album_id)
    else:
        form = PhotoForm()
    return render(request, "add_foto.html", {"form": form})


