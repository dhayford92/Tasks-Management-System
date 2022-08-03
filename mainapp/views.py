from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import View
from .models import *
from authentication.models import *
from django.urls import reverse
from django.contrib import messages


# args=(project.id,)
class DashboardAdmin(View):
    above_users = []
    
    def get(self, request):
        mytask = Task.objects.filter(assign__id__exact=request.user.id)
        users_staf = User.objects.filter(is_staff=True)
        complet_work = Project.objects.filter(status='Done')
        new_work = Project.objects.filter(status='Pending').count()
        all_project = Project.objects.all()
            
                
        context = {
            'mytask_count': mytask.count(),
            'staff_count': users_staf.count(),
            'complete_count': complet_work.count(),
            'all_project': all_project,
            'new_project_count': new_work,
            'task_user_count': len(self.above_users) - 3,
        } 
        return render(request, 'admin/admindash.html', context)
    
    
    
# Project View  

class AddProject(View):
    def get(self, request):
        prior = priority
        users = User.objects.filter(is_staff=True)
        stats = status
        context = {
            'priors': prior,
            'users': users,
            'status': stats
        }
        return render(request, 'admin/addproject.html', context)
    
    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        stat = request.POST['stat']
        prior = request.POST['prior']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        selectedusers = request.POST.getlist('userlist[]')
        
        if request.FILES['imagefile']:
            imagefile = request.FILES['imagefile']
        else:
            imagefile = ''
            
        users = User.objects.filter(id__in=selectedusers)
            
        
        try:
            project = Project.objects.create(creater=request.user, title=title, status=stat,priority=prior,start_date=startdate, due_date=enddate)
            if stat == "Done":
                project.progress = 100
            elif stat == "Working":
                project.progress = 35
            elif stat == "Cancel":
                project.progress = 0
            else:
                project.progress = 15
                
            for user in users:
                project.users.add(user)
                
            project.profile_image = imagefile
            project.description = description
            project.save()
            messages.success(request, 'Project Added Successfully')
        except:
            messages.error(request, 'Error adding new Project')
        return HttpResponseRedirect(reverse('addproject'))
    
    
class ProjectDetail(View):
    def get(self, request, id):
        project = Project.objects.get(id=id)
        prior = priority
        users = User.objects.all()
        stats = status
        context = {
            'priors': prior,
            'users': users,
            'status': stats,
            'project': project
        }
        return render(request, 'admin/editproject.html', context)
    
    def post(self, request, id):
        pass



def finishProject(request, id):
    try:
        project = Project.objects.get(id=id)
        project.status = "Done"
        project.due = "Done"
        project.save()
        messages.success(request, f"{project.title} is set to completed")
    except:
        messages.warning(request, "Project does not exists")
    return HttpResponseRedirect('allproject')


def allProject(request):
    all_project = Project.objects.all()
    context = {
        'projects': all_project,
    }
    return render(request, 'admin/allproject.html', context)
    

def deleteProject(request, id):
    try:
        project = Project.objects.get(id=id)
        project.delete()
        messages.success(request, "Project has been successfully deleted")
    except:
        messages.warning(request, "Project does not exists")
    return redirect('allproject')



# Task View
class AddTask(View):
    def get(self, request, id):
        project = Project.objects.get(id=id)
        prior = priority
        stats = status
        dues = due
        context = {
        'project': project,
        'priors': prior,
        'status': stats,
        'dues': dues,
        }
        return render(request, 'admin/addtasks.html', context)
    
    def post(self, request, id):
        title = request.POST['title']
        stat = request.POST['status']
        prior = request.POST['prior']
        due = request.POST['due']
        selectedusers = request.POST.getlist('userlist[]')
            
        users = User.objects.filter(id__in=selectedusers)
        project = Project.objects.get(id=id)    
        try:
            task = Task.objects.create(project=project, task_name=title, status=stat, priority=prior)
            
            if project.start_date == project.due_date:
                task.due = "Due"
            elif project.start_date > project.due_date:
                task.due = "Overdue"
            else:
                task.due = due
            
            if stat == "Done":
                project.progress += 20
            elif stat == "Working":
                project.progress += 10
            elif stat == "Cancel":
                project.progress += 0
            else:
                project.progress += 5
                
            for user in users:
                task.assign.add(user)
                
            task.save()
            project.save()
            messages.success(request, 'Task Added Successfully')
        except:
            messages.error(request, 'Error adding new task')
        return HttpResponseRedirect(reverse('alltask'))
    
    
class ViewTask(View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=user)
        try:
            projects = Project.objects.filter(users__id__exact=user.id)
            for obj in projects:
                project = obj.id
            tasks = Task.objects.filter(assign__id__exact=user.id, project__id__exact=project)
            context = {
                'profile': profile,
                'projects': projects,
                'tasks': tasks
            }
        except:
            context = {}
        return render(request, 'admin/alltask.html', context)
    
    def post(self, request):
        tasklist = request.POST.getlist('tasklist[]')
        
        tasks = Task.objects.filter(id__in=tasklist)
        
        for task in tasks:
            task.delete()
        messages.success(request, 'Task Successfully Deleted')
        return HttpResponseRedirect('alltask')



class EditTask(View):
    def get(self, request, id, taskId):
        project = Project.objects.get(id=id)
        task = Task.objects.get(id=taskId)
        prior = priority
        stats = status
        dues = due
        context = {
        'project': project,
        'priors': prior,
        'status': stats,
        'dues': dues,
        'task': task
        }
        return render(request, 'admin/edittask.html', context)
    
    def post(self, request, id, taskId):
        title = request.POST['title']
        stat = request.POST['status']
        prior = request.POST['prior']
        due = request.POST['due']
        selectedusers = request.POST.getlist('userlist[]')
            
        users = User.objects.filter(id__in=selectedusers)
        project = Project.objects.get(id=id)
            
        try:
            task = Task.objects.get(id=taskId)
            if project.start_date == project.due_date:
                task.due = "Due"
            elif project.start_date > project.due_date:
                task.due = "Overdue"
            else:
                task.due = due
            
            task.task_name=title
            task.priority=prior
            task.project=project
            if task.status == stat:
                pass
            else:
                if stat == "Done":
                    project.progress += 20
                elif stat == "Working":
                    project.progress += 10
                elif stat == "Cancel":
                    project.progress += 0
                else:
                    project.progress += 5
                
            for user in users:
                task.assign.add(user)
            
            task.status=stat    
            task.save()
            project.save()
            messages.success(request, 'Task Updated Successfully')
        except:
            messages.error(request, 'Error updating task')
        return HttpResponseRedirect(reverse('alltask'))