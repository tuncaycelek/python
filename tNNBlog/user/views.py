from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages

# Create your views here.

def register(request):
    form = forms.RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request, 'Hoşgeldin ' + username + '!')
        return redirect("index")

    return render(request,"register.html",{ "form" : form})

def loginUser(request):
    form = forms.LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)
        if user is None:
            messages.warning(request,"Kullanıcı adı veya parola hatalı!")
            return render(request,"login.html",{ "form" : form})
        
        messages.success(request,"Hoşgeldin " + username + "!")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",{ "form" : form })

def logoutUser(request):
    logout(request)
    messages.info(request,"Hoşçakal..! ")
    return redirect("index")
