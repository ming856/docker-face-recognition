from distutils.command.upload import upload
from django.db import models

# Create your models here.

class license(models.Model):
    license = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

class face(models.Model):
    img = models.ImageField(upload_to = 'temp/')