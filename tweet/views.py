from django.shortcuts import render
from tweet.models import Tweet_Model, MyUser
from django.contrib.auth.decorators import login_required
from tweet.forms import TweetForm
from django.shortcuts import HttpResponseRedirect, reverse, render

# Create your views here.
def tweet_view(request):
    tweet = Tweet_Model.objects.all()
    return render(request, "index.html", {"tweet": tweet})

def tweet_details(request, tweet_id):
    tweet = Tweet_Model.objects.filter(id=tweet_id).first()
    return render(request, "tweet.html", {"tweet": tweet})

def user_details(request, user_id):
    user = MyUser.objects.filter(id=user_id).first()
    return render(request, "user.html", {"user": user})

@login_required
def tweet_form(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet_Model.objects.create(
                body = data.get("body"),
                author = request.user,
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = TweetForm()
    return render(request, "new_tweet.html", {"form": form})
