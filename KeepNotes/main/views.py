from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, InsertNewNotes
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

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
                
                user = User.objects.create(
                    username = name,
                    email = email,
                    password = password
                )
                login(request, user)
                
                return redirect('user-dashboard')
                
                # print ("email already exixt")
            else:
                
                messages.error(request, 'This Email already exixt.')
            
            
    else:
        form  = UserRegistrationForm()
        
    return render(request, 'singup.html', {'form': form})

def UserLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # useremail = form.cleaned_data['user_email']
            # userpassword = form.cleaned_data['user_password']
            # user = User.objects.filter(email = useremail) 
            # if user.password == userpassword:
                
            login(request,)
            return redirect('user-dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'singin.html', {'form':form})

def user_dashboard(request):
    return render(request, 'user-dashboard.html')

def insertNotes(request):
    
    if request.method == 'POST':
        forms = InsertNewNotes(request.POST)
        if forms.is_valid():
            notes_title = forms.cleaned_data['notes_title']
            notes_content = forms.cleaned_data['notes_content']
    else:
        form = InsertNewNotes()
            
    
    return render(request, 'insertNotes.html', {'form':form})


