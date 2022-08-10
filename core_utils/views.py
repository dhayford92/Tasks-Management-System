from django.shortcuts import render, redirect

from authentication.models import Profile
from .models import *
from django.views import View
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages

    
def creatThread(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('chats', )
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('chats')
            
            if username != None:
                thread = ThreadModel(user=request.user, receiver=receiver)
                thread.save()
                return redirect('chats')
        except :
            messages.error(request, "Thread does not exists")
    else:
        messages.error(request, "Thread does not exists")
    return redirect('chats')
    
    
    
    
class ChatView(View):
    def get(self, request):
        receiver = request.GET.get('receiver')
        users = Profile.objects.all()
        message_count = MessageModel.objects.filter(is_read=False)
        print("User name is ", receiver)
        if receiver != None:
            profile = Profile.objects.get(user=receiver)
            thread = ThreadModel.objects.get(user=request.user, receiver=receiver)
        else:
           profile = None
           thread = None
        threads = ThreadModel.objects.filter(user=request.user, receiver=receiver)
        chats = MessageModel.objects.filter(receiver_user=receiver)
        context = {
            'threads': threads,
            'chats': chats,
            'users': users,
            'profile': profile,
            'thread': thread,
            'message_count': message_count.count(),
        }
        return render(request, "admin/chat.html", context)
    
    
    def post(self, request):
        thread = request.POST.get('thread')
        receiver = request.POST.get('receiver')
        message = request.POST.get('message')
        
        if message == None:
            messages.warning(request, "No message sent")
        else:
            chat = MessageModel(
                thread=thread,
                sender_user=request.user, 
                receiver_user=receiver, body=message)
            chat.save()
        return redirect('chats')
    
    
    
    
def searchThreadUser(request, *args, **kwargs):
    pass