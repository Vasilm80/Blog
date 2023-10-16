from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post (models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()

    categories = models.ManyToManyField('Category', related_name='posts')

class Coments(models.Model):
    autor = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.PROTECT, null=True )



