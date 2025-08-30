from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def singUp(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['user_name'], form.cleaned_data['user_email'])
            name = form.cleaned_data['user_name']
            email = form.cleaned_data['user_email']
            password = form.cleaned_data['user_password']
            
            check_email = User.objects.filter(email = email)
            if not check_email:
                
                User.objects.create(
                    username = name,
                    email = email,
                    password = password
                )
                
                # print ("email already exixt")
            else:
                
                messages.error(request, 'This Email already exixt.')
            
            
    else:
        form  = UserRegistrationForm()
        
    return render(request, 'singup.html', {'form': form})

def user_dashboard(request):
    return render(request, 'user-dashboard.html')
