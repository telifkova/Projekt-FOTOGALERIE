from django.forms import ModelForm

from .models import Album
from .models import Photo


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ["user"]



class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ["album"]
