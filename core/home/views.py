from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from userauth.models import Profile
from django.contrib.auth.models import User
from tasks.models import Task
# Create your views here.

@login_required(login_url='/login')
def home(request):
    profiles =  Profile.objects.all()
    tasks = Task.objects.filter(user= request.user.id)[:4]
    context = {
        'profiles':profiles,
        'tasks':tasks
    }
    return render(request, 'home/home.html', context)

# def email(request):
#     return render(request, 'home/email.html')

def timeline(request, slug):
    user = User()
    timeline =  get_object_or_404(Profile, slug=slug)
    tasks = Task.objects.filter(user=timeline.user)[:3]
    context ={
        'data':timeline,
        'tasks':tasks
    }
    return render(request, 'timeline/timeline.html', context)