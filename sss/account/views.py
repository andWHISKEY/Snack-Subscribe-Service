# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user=User.objects.get(username=request.POST['userID'])
                return render(request,"home.html",{'error1736':'error'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST["userID"],password=request.POST["password1"]
                )
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,"home.html",{'error1219':'error'})        
    return render(request,'home.html')

def login(request):
    if request.method =="POST":
        userID=request.POST['userID']
        password=request.POST.get('password1','')
        user = auth.authenticate(request,username=userID, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,"home.html",{'error0704':'error'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')