from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserLoginForm, InsertNewNotes, EditeUserInformationForm
from django.contrib.auth.models import User
from .models import Notes, UserInfos
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Global variables
# NOTES = Notes()
# USER_ID = 0

# Views 
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
        
    return redirect('login')

@login_required
def user_dashboard(request):
    user = request.user
    context = {
        "Notes":Notes.objects.filter(user_id = user),
        "user" : UserInfos.objects.filter(id=request.user.id)
    }
    print(context.get("Notes"))
    
    return render(request, 'user-dashboard.html', context)
@login_required
def insertNotes(request):
    user = request.user
    if request.method == 'POST':
        form = InsertNewNotes(request.POST)
        if form.is_valid():
            # notes_title = form.cleaned_data['notes_title']
            # notes_content = form.cleaned_data['notes_content']
            # # user = User.objects.filter(id = user_id)
            # Notes.objects.create(
            #     notes_title = notes_title,
            #     notes_text = notes_content, 
            #     user_id = user
            # )
            
            note_instance = form.save(commit=False)
            
            note_instance.user_id = user
            note_instance.save()
            
            
            return redirect('user-dashboard')
    else:
        form = InsertNewNotes()   
    
    return render(request, 'insertNotes.html', {'form': form})
@login_required
def EditeNotes(request, notes_id):
    
    note_to_edite = get_object_or_404(Notes, pk = notes_id, user_id=request.user)
    
    if request.method == 'POST':
        form = InsertNewNotes(request.POST, instance=note_to_edite)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('user-dashboard')
    else:
        form = InsertNewNotes(instance = note_to_edite)
    
    return render(request, 'editeNotes.html', {"form": form})

def DeleteNotes(request, note_id):
    Notes.objects.filter(id=note_id).delete()
    return redirect('user-dashboard')

@login_required
def user_profile(request):
    
    context = {
        'user': UserInfos.objects.filter(id = request.user.id)
    }
    
    return render(request, 'user_profile.html', context)

@login_required
def EditeUserProfile(request):
    user_infos = get_object_or_404(UserInfos, user_id= request.user)
    if request.metod == "POST":
        form = EditeUserInformationForm(request.POST, instance=user_infos)
        
        if form.is_valid():
            
            return redirect('user-profile')
    
    else:
        form = EditeUserInformationForm(instance=user_infos)
            
    return render(request, 'user_profile.html', {'form': form})

@login_required
def SettingsPage(request):
    context = {
        'user': UserInfos.objects.filter(id = request.user.id)
    }
    return render(request, 'settings.html', context)

