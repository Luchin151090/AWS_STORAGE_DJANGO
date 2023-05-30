from django.db import models
from django.utils import timezone


def user_directory_path(ejemplar,nombre_archivo):
    return 'posts/{0}/{1}'.format(ejemplar.id,nombre_archivo)


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=250)
    image = models.ImageField(upload_to=user_directory_path)
    image_caption = models.CharField(max_length=100,default='Photo Demo')
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo