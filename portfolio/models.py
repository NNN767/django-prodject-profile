from django.db import models

# Create your models here.

class  Project(models.Model): #класс models позволяет работать и связываться с бозой данных создовать
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/',max_length=50) # upload_to обозначает в какой директории будут сохроняться изображения



