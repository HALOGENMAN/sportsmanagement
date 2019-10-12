from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,"home.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if True:
            #User.objects.filter(password = password).exists() and User.objects.filter(username=username).exists()
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("dashbord")
            else:
                messages.info(request,"user doesnot is None")
                return render(request,"login.html")
        else:
            messages.info(request,"username or password does not exist ")
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return render(request,"home.html")

def create(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(email=email).exists() and User.objects.filter(username=username).exists():
                messages.info(request,"password email or username already exist")
                return render(request,"create.html")
            else:
                user = User.objects.create_user(username=username,email=email,first_name=firstname,password=password1)
                if user is not None:
                    user.save()
                    return redirect("login")
                else:
                    messages.info(request,"user is None")
                    return render(request,"create.html")   
        else:
            messages.info(request,"password did not matched")
            return render(request,"create.html")
        
       
    else:
        return render(request,"create.html")
    
def dashbord(request):

    return render(request,"dashbord.html")