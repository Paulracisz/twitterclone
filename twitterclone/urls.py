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
from twitteruser import views
from tweet.views import tweet_view, tweet_details, user_details, tweet_form

urlpatterns = [
    path('', views.index, name="homepage"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logoutview'),
    path('signup/', views.signup_view, name='signup'),
    path('feed/', tweet_view, name='feed'),
    path('tweet/<int:tweet_id>', tweet_details, name='tweet'),
    path('user/<int:user_id>', user_details, name="user"),
    path('new_tweet/', tweet_form, name="tweet_form"),
    path('admin/', admin.site.urls),
]
