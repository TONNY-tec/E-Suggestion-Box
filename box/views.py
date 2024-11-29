from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from box.forms import BoxForms, LoginForm, RegisterForm
from box.models import Box


# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
                # Redirect to the desired page after successful login
                return redirect('index')  # Replace 'home' with your desired URL name
            else:

                # Handle authentication failure
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
@login_required  # Require user logged in before they can access profile page
def posts(request):
    if request.method == 'POST':
        form = BoxForms(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            details = form.cleaned_data['details']
            form.save()
            return redirect('my_posts')
    else:
        form =  BoxForms()
    return render(request, 'posts.html', {'forms':form})
@login_required
def my_posts(request):
    data = Box.objects.all()
    context = {'data': data}
    return render(request, 'my_posts.html', context)
