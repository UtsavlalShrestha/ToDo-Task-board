from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, RegisterForm
from django.contrib import messages
from .models import Task
from django.utils import timezone




# Create your views here.
def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context= {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    if request.method == 'POST':
        if request.POST.get('Logout')=='Logout':
            logout(request)
            return redirect('home')
        else:
            return redirect('home')
    context = {}
    return render(request, 'base/logout.html', context)

def signupUser(request):
    form = RegisterForm()
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid form')
    context = {'form':form}
    return render(request, 'base/login_register.html', context)

@login_required(login_url= 'login')
def addTask(request):
    form  = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Don't save yet
            task.user = request.user        # Set the user
            task.save() 
            messages.success(request, "Added task successfully")

            return redirect('home')
        else:
            messages.error(request, "Error adding task")
    context={'form': form}
    return render(request, 'base/addTask.html', context)

def home(request):
    now = timezone.now().date()  # Get the current date, ignoring the time
    expired_tasks = Task.objects.filter(deadline__lt=now) #lt bhaneko less than
    expired_tasks.update(status='deleted')
    tasks = Task.objects.filter(status='todo')

    context={'tasks': tasks}
    return render(request, 'base/home.html', context)



def inprogress(request):
    tasks= Task.objects.filter(status = 'inprogress')
    context = {'tasks': tasks}
    return render(request, 'base/inprogress.html', context)

def completed(request):
    tasks = Task.objects.filter(status  = 'completed')
    context = {'tasks': tasks}
    return render(request, 'base/completed.html', context)

def deleted(request):
    tasks =Task.objects.filter(status = 'deleted')
    context={'tasks': tasks}
    return render(request, 'base/deleted.html', context)

def change_p(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'inprogress'
    task.save()
    return redirect('inprogress')

def changeto_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'completed'
    task.save()
    return redirect('completed')

def changeto_deleted(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'deleted'
    task.save()
    return redirect('deleted')