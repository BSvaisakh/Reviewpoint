from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    director=models.CharField(max_length=30)
    cast=models.CharField(max_length=300)
    release_date=models.DateField()
    image=models.URLField(default = None,null = True)
    
    def __str__(self):
        return self.title