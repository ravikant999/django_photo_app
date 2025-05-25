from django import forms
from .models import Upload

'''class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['image', 'description']'''

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['image', 'text'] 


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
