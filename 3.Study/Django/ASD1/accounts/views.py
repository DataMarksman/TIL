from multiprocessing import context
from ssl import HAS_TLSv1_1
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('JJangjunho:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html', context)
    

def logout(request):
    auth_logout(request)
    return redirect('JJangjunho:index')


def signup(request):
    if request.method == 'POST':
        pass
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'JJangjunho/signup.html', context)