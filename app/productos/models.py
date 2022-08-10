from django.db import models
from django.core.files import File
# Create your models here.
class productos(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=700)
    precio = models.DecimalField(max_digits=6, decimal_places=3)
    imagen = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.imagen:
            return 'http://127.0.0.1:8000'+self.imagen.url
