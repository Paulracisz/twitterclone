"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views as view
from twitteruser import views as user_views 
from tweet.views import tweet_view, tweet_details, user_details, tweet_form
from notification import views as notif_v

urlpatterns = [
    path('', tweet_view, name='homepage'),
    path('login/', view.login_view, name="login"),
    path('logout/', view.logout_view, name='logoutview'),
    path('signup/', view.signup_view, name='signup'),
    path('tweet/<int:tweet_id>/', tweet_details, name='tweet'),
    path('user/<int:user_id>/', user_details, name="user"),
    path('new_tweet/', tweet_form, name="tweet_form"),
    path('follow/<int:follow_id>/', user_views.following, name="following"),
    path('unfollow/<int:unfollow_id>/', user_views.unfollowing, name="unfollowing"),
    path('notification/', notif_v.see_notification, name="notification"),
    path('admin/', admin.site.urls),
]
