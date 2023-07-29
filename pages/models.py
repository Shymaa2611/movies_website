from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Genre(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='movies/')
    quality=models.CharField(max_length=5)
    price=models.CharField(max_length=20)
    created_At=models.DateField(auto_now_add=True)
    duration=models.IntegerField(default=0)
    #genre=models.ForeignKey(Genre,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.title

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,blank=True,null=True)
    stars=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return str(self.movie.title)
    class Meta:
        unique_together=(('user','movie'))
        index_together=(('user','movie'))


