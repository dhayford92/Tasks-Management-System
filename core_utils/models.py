from django.db import models
from django.contrib.auth.models import User

from mainapp.models import Project, Task


class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    
    
class MessageModel(models.Model):
    thread = models.ForeignKey(ThreadModel, related_name="+", on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="message", blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    
class NotificationModel(models.Model):
    notification_type = models.IntegerField()
    title = models.CharField(max_length=250, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_from", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    isSeen = models.BooleanField(default=False)
    create_on = models.DateTimeField(auto_now_add=True)