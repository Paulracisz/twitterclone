from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponseForbidden
from twitteruser.forms import LogInForm, AddUserForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = LogInForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def signup_view(request):
        if request.method == "POST":
            form = AddUserForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                TwitterUser.objects.create_user(
                    username = data.get("username"),
                    password = data.get("password"),
                )
            return HttpResponseRedirect(reverse("homepage"))
        form = AddUserForm()
        return render(request, "generic_form.html", {"form": form})