from django.contrib import messages, auth
from django.shortcuts import render

from django.contrib.auth.models import User

from django.shortcuts import render, redirect

def student(request):
    return render(request,'student.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('loginapp:student')
        else:
            messages.info(request, "invalid credentials")
        return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if cpassword == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('register.html')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();

                return redirect('login')
                print("user created")

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):
    return render(request,'form.html')
def about(request):
    return render(request,'aboutus.html')





