from django.db import models
from twitteruser.models import TwitterUser
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
    body = models.CharField(max_length=140, default="")
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    time_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.body



