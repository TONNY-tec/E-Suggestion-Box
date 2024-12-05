import os

from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context

import box
from box.forms import BoxForms , RegisterForm
from box.models import Box, Comment


# my views.
def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def create_posts(request):
    if request.method == 'POST':
        form = BoxForms(request.POST, request.FILES)
        if form.is_valid():
            box =form.save(commit=False)
            box.user = request.user
            box.save()
            return redirect('create_posts')
    else:
        form =  BoxForms()
    return render(request, 'create_posts.html', {'form':form})

def posts(request):
    data = Box.objects.all()
    context = {'data':data}
    return render(request, 'posts.html', context)

@login_required
def my_posts(request):
    data = Box.objects.filter(user=request.user)  # Filter by logged-in user
    context = {'data': data}
    return render(request, 'my_posts.html', context)

@login_required
def update(request, id):
    box = get_object_or_404(Box, id=id)
    if request.method == 'POST':
        form = BoxForms(request.POST, request.FILES, instance=box)
        if form.is_valid():
            form.save()

            if 'image' in request.FILES:
                file_name = os.path.basename(request.FILES['image'].name)
                messages.success(request,'Post updated successfully! {file_name}uploaded')
            else:
                messages.error(request,'Post details updated successfully!')
            return redirect('posts')
        else:
            messages.error(request,'Please confirm your changes')
    else:
        form = BoxForms(instance=box)
    return render(request, 'update.html',{'form': form, 'box': box} )

@login_required
def comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:  # Check if comment is not empty
            post_id = request.POST.get('post_id')  # Get the post ID from the form
            post = get_object_or_404(Box, id=id)
            comment = Comment.objects.create(comment=comment_text, user=request.user, post=post)
            comment.save()
            return redirect('my_posts')  # Redirect to user's posts after adding comment
    else:
        return redirect('my_posts')  # Redirect if not a POST request

# def update(request, id):
#     box = get_object_or_404(Box, id=id)
#
#     if request.method == 'POST':
#         form = BoxForms(request.POST, request.FILES, instance=box)  # Pre-populate the form with existing data
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your post "{box.title}" has been updated!')
#             return redirect('my_posts')  # Redirect to user's posts after update
#     else:
#         form = BoxForms(instance=box)  # Create form with existing post data for editing
#
#     context = {'form': form, 'post': box}
#     return render(request, 'update.html', context)

def delete(request, id):
    customer = get_object_or_404(Box, id=id)
    try:
        customer.delete()
        messages.success(request,'Customer deleted successfully!')
    except Exception as e:
        messages.error(request,'Error deleting customer')
    return redirect('about')

# def post_detail(request, post_id):
#     post = get_object_or_404(Box, pk=post_id)
#     comments = post.comments.order_by('-created_date')  # Order comments by creation date (descending)
# @login_required
# def post_detail(request, post_id):
#     post = get_object_or_404(Box, pk=post_id)
#     comments = post.comments.order_by('-created_date')
    # Order comments by creation date (descending)


# @login_required
# def post(request, post_id):
#     post = get_object_or_404(Comment, pk=post_id)
#     comments = post.comment.all()
#
#     if request.method == 'POST':
#
#         comment_form = BoxForms(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.user= request.user  # Assuming user authentication is set up
#             comment.save()
#             return redirect('post', post_id=post_id)
#     else:
#         comment_form = BoxForms()
#
#     context = {'post': post, 'comments': comments, 'comment_form':comment_form}
#     return render(request, 'post.html',context)