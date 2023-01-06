from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from anasayfa.forms import UpdateUserForm


@login_required
def ProfileCustomize(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'users/profile.html', {'user_form': user_form})


def IndexView(request):
    return render(request, 'main.html', {
        'username': 'test user'
    })

def LogOutView(request):    
    return render(request, 'logoutsuccess.html')

def AboutUsView(request):
    return render(request, 'about.html')

def ProfileView(request):
    return render(request, 'user.html')

def ContactView(request):
    return render(request, 'contactUs.html')