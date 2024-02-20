from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_album, name="add_album"),
    path("album/<int:album_id>", views.detail, name="detail"),
    path("accounts/registration/", views.registration, name="registration"),
]