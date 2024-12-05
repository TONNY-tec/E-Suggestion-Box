from django.urls import path
from django.contrib.auth import views as auth_views
from box import views
# from users import views as user_views
from box.views import my_posts

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name ='register'),
    path('posts/', views.posts, name='posts'),
    path('create_posts/', views.create_posts, name='create_posts'),
    path('my_posts/', my_posts, name='my_posts'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/',views.delete,name='delete'),
    path('comment/',views.comment, name='comment'),

]