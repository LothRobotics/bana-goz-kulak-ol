from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request, 'main.html')

def LogOutView(request):    
    return render(request, 'logoutsuccess.html')

def AboutUsView(request):
    return render(request, 'about.html')