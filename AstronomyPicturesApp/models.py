from django.db import models


# Create your models here.

class Picture(models.Model):
    title=models.CharField(max_length=500)
    url=models.CharField(max_length=500)
    hdurl=models.CharField(max_length=500)
    explanation=models.TextField()