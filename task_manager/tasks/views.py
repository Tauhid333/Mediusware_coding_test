from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def sys_login(request):
    if request.user.is_authenticated: 
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next")
            return redirect("home") if not next_url else redirect(next_url)
        else: pass
    return render(request, "login.html")

def sys_logout(request):
    logout(request)
    return redirect('login')  

@login_required
def home(request):
    context = {
        
    }
    return render(request, "home.html",context)

try : from tasks.view.task import *
except ImportError : pass
