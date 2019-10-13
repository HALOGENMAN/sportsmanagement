from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class dashbord(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=20,default="")
    single_player = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name
