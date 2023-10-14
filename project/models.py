from django.db import models

# Create your models here.

class myproject(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    technology = models.CharField(max_length=50)



