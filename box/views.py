from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def posts(request):
    return render(request, 'posts.html')
def my_posts(request):
    return render(request, 'my_posts.html')