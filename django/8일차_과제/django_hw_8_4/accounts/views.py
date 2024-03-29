from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login   
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    accounts = User.objects.all()
    context = {
        'accounts' : accounts
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == 'POST':    # 로그인 로직 진행이라면
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:   # 로그인 페이지 GET
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')