from django.db import models
from django.contrib.auth.models import User

# Create your models here.

###############MOVIES##########################

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    director=models.CharField(max_length=30)
    cast=models.CharField(max_length=300)
    release_date=models.DateField()
    avearge_rating=models.FloatField(default=0)
    image=models.URLField(default = None,null = True)
    
    def __str__(self):
        return self.title
##############################################################

########################SERIES################################
 
class Series(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    creators=models.CharField(max_length=30)
    cast=models.CharField(max_length=300)
    avearge_rating=models.FloatField(default=0)
    ONGOING = 'ongoing'
    FINISHED = 'finished'
    STATUS_CHOICES = [
        (ONGOING, 'Ongoing'),
        (FINISHED, 'Finished'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ONGOING)
    seasons = models.IntegerField()
    episodes = models.IntegerField()
    image=models.URLField(default = None,null = True)
    
    def __str__(self):
        return self.title
    
class Anime(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    Author = models.CharField(max_length=50)
    avearge_rating=models.FloatField(default=0)
    ONGOING = 'ongoing'
    FINISHED = 'finished'
    STATUS_CHOICES = [
        (ONGOING, 'Ongoing'),
        (FINISHED, 'Finished'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ONGOING)
    episodes = models.IntegerField()
    image=models.URLField(default = None,null = True)
    
    def __str__(self):
        return self.title
    
    
class MovieReview(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length = 1000)
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.user.username 
    
class SeriesReview(models.Model):
    series = models.ForeignKey(Series,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length = 1000)
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.user.username 
    
class AnimeReview(models.Model):
    anime = models.ForeignKey(Anime,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length = 1000)
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.user.username 