from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    admin = models.CharField(max_length = 255, null= True, blank = True)
    description = models.CharField(max_length = 255, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



class Message(models.Model):
    content = models.CharField(max_length = 255, null = True, blank = True)
    user_id = models.ForeignKey(User, related_name="usermessage", on_delete = models.CASCADE)
    visitor_id = models.ForeignKey(User, related_name="visitormessage", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Comment(models.Model):
    content = models.CharField(max_length = 255, null = True, blank = True)
    message_id = models.ForeignKey(Message,  related_name="messagecomment", on_delete = models.CASCADE)
    user_id = models.ForeignKey(User,  related_name="commentuser", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
