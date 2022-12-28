from django.shortcuts import render

def IndexView(request):
    return render(request, 'main.html')

def LogOutView(request):    
    return render(request, 'logoutsuccess.html')

def AboutUsView(request):
    return render(request, 'about.html')

def ProfileView(request):
    return render(request, 'profile.html')