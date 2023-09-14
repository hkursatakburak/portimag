from django.shortcuts import render, redirect
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from topics.models import Topic
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password= password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Giris engellendi!')
            else:
                messages.info(request, 'Şifre ya da kullanıcı adı yanlış!')
    else:
        form = LoginForm()
               
    return render(request, 'login.html', {'form' : form})
    

def user_register(request):
     
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kullanıcı kaydedildi!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form' : form})



def user_logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url="login")
def user_dashboard(request):
    current_user = request.user

    topics = current_user.konu_takip.all()
    context = {
        'topics' : topics
    }
    return render(request, "dahsboard.html", context)


def enroll_the_topic(request):
    topic_id = request.POST['topic_id']
    user_id = request.POST['user_id']
    topic = Topic.objects.get(id = topic_id)
    user = User.objects.get(id = user_id)
    topic.students.add(user)
    return redirect('dashboard')