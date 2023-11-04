from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario','class': 'lg-username',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña','class': 'lg-passwd',}))

    class Meta:
        model = User
        fields = ['username','password']

class RegisterForm(UserCreationForm):

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your username',
                                                             'class': 'rg-username',
                                                             'autocomplete':'off',
                                                             }))
    
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password',
                                                                  'class': 'rg-passwd',
                                                                  'data-toggle': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password',
                                                                  'class': 'rg-passwd-conf',
                                                                  'data-toggle': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['username','password1', 'password2']

