from django.shortcuts import redirect, render
from .models import *

from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request): 
    if request.user.is_authenticated:
        return redirect('home')   
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)     
            error = form.errors
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            print('Username: ', username,  '  password1: ', password1, '  password2: ', password2)
            print(error)
            messages.success(request, 'Acount was created for ' + username)
            if form.is_valid():
                form.save()
                print('Success')
                return redirect('login')
            else:
                print('Failing..')    
        else:
            form = CreateUserForm()     
            error = ''
        context = {
            'form': form, 
            'error': error
        }
        return render(request, 'registrate/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')   
    else:
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')             
        
    return render(request, 'registrate/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


            
