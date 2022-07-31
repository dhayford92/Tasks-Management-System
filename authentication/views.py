from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from .models import Profile, Skills
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage


class Login(View):
    def get(self, request):
        return render(request, 'authen/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user !=None:
            login(request, user)
            if user.first_name == '':
                return redirect('setname')
            else:
                return redirect('admindash')
        else:
            messages.error(request, "Invalid credentials")
        return render(request, 'authen/login.html')
    
    

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')



class SetName(View):
    def get(self, request):
        return render(request, 'authen/setname.html')
    
    def post(self, request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        if request.FILES['imagefile']:
            imagefile = request.FILES['imagefile']
        try:
            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            # fss = FileSystemStorage()
            # file = fss.save(imagefile.name, imagefile)
            profile.profile_image = imagefile
            profile.save()
            
            messages.success(request, 'Full Name Set Successfully')
            return redirect('admindash')
        except:
            messages.error(request, 'Full Name Set Failed')
            return HttpResponseRedirect('setname')





class ProfileView(View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=user)
        skills = Skills.objects.filter(user=user)
        context = {
            'profile': profile,
            'user': user,
            'skills': skills
        }
        return render(request, 'authen/profile.html', context)
    
    def post(self, request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        location = request.POST['location']
        bio = request.POST['bio']
        description = request.POST['description']
        
        if request.FILES['imagefile']:
            imagefile = request.FILES['imagefile']
        
        try:
            user = User.objects.get(id=request.user.id)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            profile = Profile.objects.get(user=user)
            profile.number = phone
            profile.profile_image = imagefile
            profile.location = location
            profile.bio = bio
            profile.description = description
            profile.save()
            messages.success(request, 'Profile Updated Successfully')
        except:
            messages.error(request, 'Profile Updated Failed')
        return HttpResponseRedirect('profile')
    
    

def updateSocial(request):
    if request.method == "POST":
        twitter = request.POST['twitter']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']
        github = request.POST['github']
        try:
            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            profile.fb_acc = twitter
            profile.tw_acc = facebook
            profile.Ig_acc = instagram
            profile.git_acc = github
            profile .save()
            messages.success(request, 'Skills Added Successfully')
        except:
            messages.error(request, 'Error adding skills')
        return HttpResponseRedirect('profile')



def addSkills(request):
    if request.method == "POST":
        skill = request.POST['skill']
        try:
            user = User.objects.get(id=request.user.id)
            sk = Skills.objects.create(user=user, title=skill)
            sk.save()
            messages.success(request, 'Skills Added Successfully')
        except:
            messages.error(request, 'Error adding skills')
        return HttpResponseRedirect('profile')