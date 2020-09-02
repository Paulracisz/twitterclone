from django.db import models
from twitteruser.models import MyUser

# Create your models here.
class Tweet_Model(models.Model):
    body = models.CharField(max_length=140, default="")
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.body

