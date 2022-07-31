from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile", null=True, blank=True, default="static/img/avatar/avatar.jpg")
    bio = models.TextField(null=True, blank=True)
    workfield = models.CharField(max_length=230, null=True, blank=True)
    number = models.CharField(max_length=230, null=True, blank=True)
    location = models.CharField(max_length=230, null=True, blank=True)
    fb_acc = models.URLField(null=True, blank=True)
    tw_acc = models.URLField(null=True, blank=True)
    Ig_acc = models.URLField(null=True, blank=True)
    git_acc = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    


class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=230, null=True, blank=True)
    achievement_point = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        instance.profile.save()