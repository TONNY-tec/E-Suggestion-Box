from typing import Any

from django.contrib.auth.models import User
from django.db import models

# my  models .

class Box(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'box_images/', blank = True, )
    details = models.CharField(max_length=200)
    def __str__(self):
        return self.details

class Comment(models.Model):
    post = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]

# class Post(models.Model):
# #     post = models.ForeignKey('Post',
# # on_delete=models.CASCADE, related_name='comments')
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#
