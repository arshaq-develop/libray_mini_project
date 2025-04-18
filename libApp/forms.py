from django import forms
from django.views import View
from libApp.models import Books
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
        }


class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['bookname', 'genre', 'author', 'image', 'status']
        widgets = {
            'bookname': forms.TextInput(attrs={'class':'form-control'}),
            'genre': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }

class BookUpdateForm(forms.ModelForm):
     class Meta:
        model = Books
        fields = ['bookname', 'genre', 'author', 'image', 'status']
        widgets = {
            'bookname': forms.TextInput(attrs={'class':'form-control'}),
            'genre': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }

