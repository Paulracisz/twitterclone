from django.shortcuts import render
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your views here.
    
def user_details(request, user_id):
    user = TwitterUser.objects.filter(id=user_id).first()
    return render(request, "user.html", {"user": user})
    
    
def following(request, follow_id):
    logged_in_user = request.user
    followed = TwitterUser.objects.filter(id=follow_id).first()
    logged_in_user.following.add(followed)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def unfollowing(request, unfollow_id):
    logged_in_user = request.user
    followed = TwitterUser.objects.filter(id=unfollow_id).first()
    logged_in_user.following.remove(followed)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))