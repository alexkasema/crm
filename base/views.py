from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, CreateEmployeeForm, UpdateEmployeeForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Staff
 
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
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'base/login.html', context)

@login_required(login_url='login')
def dashboard(request):

    employees = Staff.objects.all()

    context = {'employees': employees}
    return render(request, 'base/dashboard.html', context)


@login_required(login_url='login')
def create_employee(request):

    form = CreateEmployeeForm()

    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {'form': form}
    return render(request, 'base/create-record.html', context)

@login_required(login_url='login')
def update_employee(request, pk):
    
    employee = Staff.objects.get(id=pk)

    form = UpdateEmployeeForm(instance=employee)

    if request.method == 'POST':

        form = UpdateEmployeeForm(request.POST, instance=employee)

        if form.is_valid():

            form.save()

            return redirect('dashboard')
    
    context = {'form': form, 'employee': employee}
    return render(request, 'base/update-record.html', context)

#! Read / view an employee record
@login_required(login_url='login')
def view_employee(request, pk):
    
    employee = Staff.objects.get(id=pk)

    context = {'employee': employee}
    return render(request, 'base/view-record.html',context)

@login_required(login_url='login')
def delete_employee(request, pk):

    employee = Staff.objects.get(id=pk)

    employee.delete()

    return redirect('dashboard')







def userLogout(request):

    logout(request)
    return redirect('login')
