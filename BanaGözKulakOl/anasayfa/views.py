from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import nameSurnameForm

def ProfileCustomize(request):
    if request.method == 'POST':
        form = nameSurnameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = nameSurnameForm()
    return render(request, 'profileCustomize.html', {'form': form})


def IndexView(request):
    return render(request, 'main.html')

def LogOutView(request):    
    return render(request, 'logoutsuccess.html')

def AboutUsView(request):
    return render(request, 'about.html')

def ProfileView(request):
    return render(request, 'user.html')