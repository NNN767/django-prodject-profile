from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    time = models.DateTimeField(auto_now=True)

class  person_img(models.Model): #класс models позволяет работать и связываться с бозой данных создовать
    image = models.ImageField(upload_to='blog/images/',) # upload_to обозначает в какой директории будут сохроняться изображения