from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']

        user = auth.authenticate(username=user, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid request')
            return redirect('userregistration.html')

    else:
        return redirect('/')

def register(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']

        if User.objects.filter(username=user).exists():
            messages.info(request,'Username taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=user, password=password)
            user.save();
            print('user created')
        return redirect('/')
    else:
        return render(request,'userregistration.html')