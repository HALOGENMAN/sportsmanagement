from django.shortcuts import render,redirect


# Create your views here.

def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def create(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        return redirect("login")
    else:
        return render(request,"create.html")