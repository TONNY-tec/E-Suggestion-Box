from django.urls import path
from django.contrib.auth import views as auth_views
from box import views
# from users import views as user_views
from box.views import my_posts

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name ='register'),
    path('posts/', views.posts, name='posts'),
    path('my_posts/', my_posts, name='my_posts'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]