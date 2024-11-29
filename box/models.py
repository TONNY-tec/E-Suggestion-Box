from django.db import models

# Create your models here.

class Box(models.Model):
    image = models.ImageField(upload_to='images/')
    details = models.CharField(max_length=200)
    def __str__(self):
        return self.details

