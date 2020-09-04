from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser

# Create your models here.
class Notification(models.Model):
    user_notified = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet_notification = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    notification_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.tweet_notification.body