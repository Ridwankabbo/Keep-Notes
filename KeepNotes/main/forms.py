from django import forms

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