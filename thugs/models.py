from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class raila(models.Model):
    bet = models.CharField(max_length=20,default=None, blank=True, null=True)
    betrs = models.IntegerField(default=None, blank=True, null=True)
    comment = models.DecimalField(max_digits = 5, 
                         decimal_places = 2,default=None, blank=True, null=True)
    author =models.CharField(max_length=20)
    coi= models.IntegerField(default=None, blank=True, null=True)
    commision=models.CharField(max_length=20,default=None, blank=True, null=True)
    class Meta:
        db_table="thugs_raila"

    
class adminbet(models.Model):
    club1= models.CharField(max_length=20)
    club2 = models.CharField(max_length=20)
    odds1 = models.DecimalField(max_digits = 5, 
                         decimal_places = 2)
    odds2 = models.DecimalField(max_digits = 5, 
                         decimal_places = 2)
    lrange = models.IntegerField()
    uprange =models.IntegerField()