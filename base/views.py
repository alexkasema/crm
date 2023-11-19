from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'base/index.html')


# TODO: Register a user
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST) #! this is saying we want to post that data

        if form.is_valid():
            form.save()

            return redirect('login')

    context = {'form': form}
    return render(request, 'base/register.html', context)

def userLogin(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                #return redirect('')
    context = {'form': form}
    return render(request, 'base/login.html', context)

def userLogout(request):

    logout(request)
    return redirect('login')
