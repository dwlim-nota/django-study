from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        email = request.POST.get("email")
        passwd = request.POST.get("passwd")
        user = User.objects.create_user(username=username, email=email, password=passwd)
        user.save()
        login(request, user)
        return redirect("pages:index")
    else:
        return render(request, 'accounts/signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        passwd = request.POST.get("passwd")
        user = authenticate(username=username, password=passwd)
        if user is not None:
            login(request, user)
        return redirect("pages:index")
    else:
        return render(request, "accounts/login.html")

def myaccount(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "accounts/myaccount.html")

def signout(request):
    if request.method == "POST":
        user = get_user(request)
        user.delete()
    return redirect("pages:index")

def user_logout(request):
    logout(request)
    return redirect("pages:index")