from django import forms
from twitteruser.models import TwitterUser

class TweetForm(forms.Form):
    body = forms.CharField(max_length=140)