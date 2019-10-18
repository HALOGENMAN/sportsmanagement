from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class dashbord(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=20)
    single_player = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class dd1(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    team = models.CharField(max_length=20,default=" ",null=True)
    
class single1(models.Model):
    name = models.CharField(max_length=50)
    team1 = models.ForeignKey(dd1,on_delete=models.CASCADE)

