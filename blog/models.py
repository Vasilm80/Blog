from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post (models.Model):
    title = models.CharField(max_length=250)
    bode = models.TextField()
    categories = models.ManyToManyField('Category', related_name='post')

class Coments(models.Model):
    autor = models.CharField(max_length=60)
    body = models.TextField()


