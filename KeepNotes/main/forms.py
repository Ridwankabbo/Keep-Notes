from django import forms
from django.contrib.auth.models import User
from .models import Notes, UserInfos, SharedNotes

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
        
class InsertNewNotes(forms.ModelForm):
    
    # notes_title = forms.CharField(
    #     widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Note title'})
    # )
    
    # notes_content = forms.CharField(
    #     widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your note content here.....'})
    # )
    
    class Meta:
        model = Notes
        fields = ['notes_title', 'notes_text']
        
        widgets = {
            'notes_title' : forms.TextInput(attrs={"class":"w-full px-4 py-3 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300", "placeholder":"Enter title"}),
            'notes_text' : forms.Textarea(attrs={"class":"fw-full px-4 py-3 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 resize-y", "placeholder":"Enter content"})
        }
        
        # def save(self, commit = True):
        #     note =  super().save(commit=False)
        #     note.set_title(self.cleaned_data['notes_title'])
        #     note.set_text(self.cleande_data['notes_text'])
            
        #     if commit :
        #         note.save()
        
class UserInformationForm(forms.ModelForm):
    
    class Meta:
        model = UserInfos
        fields = [ 'user_imge', 'user_email']
        
        widgets={
            'user_imge' : forms.FileInput(attrs={'class':'p-3', 'placeholder':'Enter our image'}),
            'user_email' : forms.EmailInput(attrs={'class':' p-3', 'placeholder':'your email'})
        }
        
class ShareNoteSForm(forms.ModelForm):
    class Meta:
        model = SharedNotes
        fields = ['share_to_user', 'permission_type']
        
        widgets = {
            'permission_type' : forms.RadioSelect(attrs={'class':'custom-radio-group'}),
        }
    
    
    
    
        
        
