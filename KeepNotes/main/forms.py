from django import forms
from django.contrib.auth.models import User
from .models import Notes

class UserRegistrationForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter name', 'id':'signup-email'})
    )
    
    user_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email'})
    )
    
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'})
    )
    
class UserLoginForm(forms.ModelForm):
    # user_email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter email'})
    # )
    # user_password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter password'})
    # )
    
    class Meta:
        model = User
        fields = ['email', 'password']
        
        widgets = {
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Enter password'})
        }
        
class InsertNewNotes(forms.Form):
    
    notes_title = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Note title'})
    )
    
    notes_content = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your note content here.....'})
    )
        
        
