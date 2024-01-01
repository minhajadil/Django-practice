from django.db import models
from Musician.models import MusicianDB
from django.utils import timezone

# Create your models here.

RATING_CHOICES = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
) 

class AlbumDB(models.Model):
    Album_Name = models.CharField(max_length=40)
    Rating = models.CharField(max_length=1 ,choices=RATING_CHOICES,default='1')
    Release_date =models.DateField(default=timezone.now)
    musician =models.ForeignKey(MusicianDB, on_delete=models.CASCADE)




