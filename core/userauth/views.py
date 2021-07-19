from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout
from .forms import loginForm
from django.contrib import messages
from .forms import profileForm, userForm

# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate( username=username,  password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"Welcome to Ennovatehub Tracking Tool {username.capitalize()}")
                return redirect('/')
                
        else:
            messages.error(request, f"Invalid Username or Password Please fill them in correctly")
            return redirect('login')
    form = loginForm()
    context = {
        'form':form
    }
    return render(request, 'auth/login.html', context)


def logout_request(request):
    logout(request)
    messages.info(request,f"logged out")
    return redirect('login')



def edit_profile(request):
    if request.method == 'POST':
        print(request.POST)
        uform = userForm(request.POST, instance=request.user)
        pform = profileForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.info(request, f"Succesful updated profile")
            return redirect('/')
    
    else:
        uform = userForm(instance=request.user)
        pform = profileForm(instance=request.user.profile)
    context = {
        'pform':pform,
        'uform':uform
    }
    return render(request, 'auth/editProfile.html', context)