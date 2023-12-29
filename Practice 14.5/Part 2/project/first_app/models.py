from django.db import models

# Create your models here.

class PracticeModel(models.Model):
    Roll = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    Bank_balance = models.BigIntegerField()
    Agree_the_term = models.BooleanField()
    Date_of_birth = models.DateField()
    Max_holding_breath = models.DurationField()
    # it needs a new pip image_field = models.ImageField(upload_to='uploads')

    #I got the idea , rest of them is pretty similar.



