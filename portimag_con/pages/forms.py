from  django import forms
from . models import Contact


class ContactForm(forms.ModelForm):
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
