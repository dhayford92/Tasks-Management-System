from ast import Assign
from django.db import models
from django.contrib.auth.models import User


status = (
    ('Pending', 'Pending'),
    ('Working', 'Working'),
    ('Done', 'Done'),
    ('Cancelled', 'Cancelled'),
)

due = (
    ('Due', 'Due'),
    ('Overdue', 'Overdue'),
    ('Done', 'Done'),
)

priority = (
    ('Low', 'Low'),
    ('High', 'High'),
    ('Average', 'Average'),
)



class Project(models.Model):
    profile_image = models.ImageField(upload_to="project", null=True, blank=True, default="static/img/avatar/avatar.jpg")
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=230)
    status = models.CharField(max_length=230, choices=status, default='Pending')
    priority = models.CharField(max_length=100, choices=priority, default='Average', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    due_date = models.DateField()
    progress = models.IntegerField(null=True, blank=True, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
        
    
    def __str__(self):
        return(self.title)    
    
        

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assign = models.ManyToManyField(User)
    task_name = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices=status, default='Pending')
    priority = models.CharField(max_length=100, choices=priority, default='Average', null=True, blank=True)
    due = models.CharField(max_length=100, choices=due, default='Due')

    class Meta:
        ordering = ['project', 'task_name']
        
    

    def __str__(self):
        return(self.task_name)