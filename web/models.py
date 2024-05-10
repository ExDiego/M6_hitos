import uuid
from django.db import models
from django.utils.text import slugify


# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    name = models.CharField(max_length=50)
    descripcion = models.TextField(blank=False, null=False)
    image = models.URLField()
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    is_private = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    # se convierte el cambio "precio" de Decimal a float antes de serializar a JSON, o me da error
    
    def to_jsonable(self): 
        return {
            "flan_uuid": str(self.flan_uuid),
            "name": self.name,
            "descripcion": self.descripcion,
            "image": self.image,
            "slug": self.slug,
            "is_private": self.is_private,
            "precio": float(self.precio), # se agrega float a self.precio
        }
    


class Contacto(models.Model):
    ContactForm_uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    customer_name = models.CharField(max_length=50, blank=False)
    customer_email = models.EmailField(blank=False)
    message = models.TextField(blank=False)
    
    def __str__(self):
        return self.customer_name