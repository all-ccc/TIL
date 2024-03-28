from django.shortcuts import render

# Create your views here.
def login(request, username, password):
     context = {
          'username' : username,
          'password' : password
     }
     return render(request, 'login.html', context )
