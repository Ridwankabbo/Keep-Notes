from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, InsertNewNotes
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def singUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['user_name'], form.cleaned_data['user_email'])
            # name = form.cleaned_data['user_name']
            # email = form.cleaned_data['user_email']
            # password = form.cleaned_data['user_password']
            
            # check_email = User.objects.filter(email = email)
            # if not check_email:
                
            #     user = User.objects.create(
            #         username = name,
            #         email = email,
            #         password = password
            #     )
            #     login(request, user)
                
            #     return redirect('user-dashboard')
                
            #     # print ("email already exixt")
            # else:
                # messages.error(request, 'This Email already exixt.')
            
            login(request, form.save())
            return redirect('user-dashboard')
            
    else:
        form  = UserCreationForm()
        
    return render(request, 'singup.html', {'form': form})

def UserLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
                
            login(request, form.get_user())
            # messages.success(request, f"Welcome back, {form.cleaned_data['username']}!")
            return redirect('user-dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'singin.html', {'form':form})

def UserLogout(request):
    
    if request.method == 'POST':
        logout(request)
        
        return redirect('index')

# @login_required()
def user_dashboard(request):
    
    return render(request, 'user-dashboard.html')

def insertNotes(request):
    
    if request.method == 'POST':
        form = InsertNewNotes(request.POST)
        if form.is_valid():
            notes_title = form.cleaned_data['notes_title']
            notes_content = form.cleaned_data['notes_content']
            # print(notes_title, notes_content)
            
            
            
            return redirect('user-dashboard')
    else:
        form = InsertNewNotes()   
        
    
    
    return render(request, 'insertNotes.html', {'form': form})


