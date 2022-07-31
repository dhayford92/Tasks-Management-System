from django.shortcuts import render
from django.views import View
from .models import *
from authentication.models import *



class DashboardAdmin(View):
    list_of_project = []
    above_users = []
    
    def get(self, request):
        users_cus = User.objects.filter(is_staff=False)
        users_staf = User.objects.filter(is_staff=True)
        complet_work = Project.objects.filter(status='Done')
        all_project = Project.objects.all()
        
        for project in all_project:
            if project.status != 'Cancelled' or project.status != 'Done':
                self.list_of_project.append(project)
                
        for task_user in all_project:
            self.above_users.append(task_user.users)
            
                
        context = {
            'customer_count': users_cus.count(),
            'staff_count': users_staf.count(),
            'complete_count': complet_work.count(),
            'all_project': all_project,
            'new_project_count': len(self.list_of_project),
            'task_user_count': len(self.above_users) - 3,
        }
                
        return render(request, 'admin/admindash.html', context)
    
    
    
    

class AddProject(View):
    def get(self, request):
        
        context = {}
        return render(request, 'admin/addproject.html', context)
    
    def post(self, request):
        pass
    

def allProject(request):
    all_project = Project.objects.all()
    
    context = {
        'projects': all_project,
    }
    return render(request, 'admin/allproject.html', context)
    

class AddTask(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass