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

class UserModel(models.Model):
    log = models.CharField(max_length=100, verbose_name='Login')
    pas = models.CharField(max_length=150, verbose_name='Password')
    email = models.CharField(max_length=200, verbose_name='E-mail')



