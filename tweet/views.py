import re

from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render, reverse
from notification.models import Notification
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser


# Create your views here.
@login_required
def tweet_view(request):
    users_tweets = Tweet.objects.filter(author=request.user)
    followed_tweets = Tweet.objects.filter(author__in=request.user.following.all())
    merged_tweets = followed_tweets | users_tweets
    return render(request, "index.html", {"tweets": merged_tweets })

def tweet_details(request, tweet_id):
    tweet = Tweet.objects.filter(id=tweet_id).first()
    return render(request, "tweet.html", {"tweet": tweet})

def user_details(request, user_id):
    user = TwitterUser.objects.filter(id=user_id).first()
    tweet = Tweet.objects.filter(author=user)
    return render(request, "user.html", {"user": user, "tweets": tweet})

@login_required
def tweet_form(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                body = data.get("body"),
                author = request.user,
            )
            reg = re.findall(r'@(\w{1,})', data.get("body"))
            for r in reg:
                match = TwitterUser.objects.filter(username=r)
                if match:
                    Notification.objects.create(
                        user_notified = match.first(),
                        tweet_notification = new_tweet
                    )
            return HttpResponseRedirect(reverse("homepage"))
    form = TweetForm()
    return render(request, "new_tweet.html", {"form": form})
