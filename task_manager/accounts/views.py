from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import UserRegisterForm

def user_login(request):
    if request.method == "POST":
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           user=form.get_user()
           login(request,user)
           return redirect("home_page")
    else:
        form = AuthenticationForm()
    data = {
        "form" : form
    }
    return render(request , "accounts/login.html" , context=data)


def register(request):
    if request.method == "POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=UserRegisterForm()
    data = {
        "form" : form
    }
    return render(request , "accounts/register.html" , context=data)
