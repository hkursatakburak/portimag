from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Ad',
    }))
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Şifre',
    }))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Ad',
    }))
    last_name = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Soyad',
    }))
    email = forms.CharField(widget= forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Email',
    }))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Şifre',
    }))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Şifreni tekrarla',
    }))

    class Meta(): 
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

"""class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'İsim',
    }))
    last_name = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Soyisim',
    }))
    email = forms.EmailField(widget= forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Email',
    }))
    about = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Ne hakkında',
    }))
    message = forms.CharField(widget= forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder' : 'Mesajınız',
    }))

    class Meta():        #meta claas ı oluşturduk ve model contact atadık fields ları yazdık bunları html dosyasında kullanmak için
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'about', 'message']
"""