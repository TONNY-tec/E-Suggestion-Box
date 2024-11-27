from django.urls import path

from box import views
from box.views import my_posts

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('posts', views.posts, name='posts'),
    path('my_posts', my_posts, name='my_posts'),
]