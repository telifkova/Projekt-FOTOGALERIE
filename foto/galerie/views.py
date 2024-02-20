from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Album
from .forms import AlbumForm

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

def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id, user_id=request.user.id)
    return render(request,"detail.html",{"album": album})