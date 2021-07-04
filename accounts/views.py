from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        name = name.split()
        first_name = name[0]
        last_name = name[1]
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        parsestring = ''
        if password != cpassword:
            parsestring += ' Password does not match. '
            print(parsestring)
        if User.objects.filter(username=username).exists():
            parsestring += 'Username taken. '
            print(parsestring)
        if User.objects.filter(email=email).exists():
            parsestring += 'email taken . '
            print(parsestring)
        if len(parsestring) > 0:
            print(parsestring)
            messages.info(request, parsestring)
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                            last_name=last_name)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request, " invalid username and password")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

