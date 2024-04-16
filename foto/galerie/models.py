from django.db import models

from django.contrib.auth.models import User



class Album(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(null = True)
    
    def get_random_photo(self):
        return self.photo_set.order_by("?").first()
        
class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(null = True)
    name = models.CharField(max_length = 100)



