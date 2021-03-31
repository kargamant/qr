from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField()
    photo = models.ImageField()
    qr = models.ImageField()




