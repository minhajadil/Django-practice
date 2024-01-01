from django.db import models

  
# specifying choices 


class MusicianDB(models.Model):
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    Email = models.EmailField()
    Phone_number= models.CharField(max_length=14)
    Instrument_type= models.CharField(max_length=14)

    def __str__(self):
        return self.First_Name
  



