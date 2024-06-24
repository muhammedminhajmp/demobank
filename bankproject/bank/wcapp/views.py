

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .forms import PersonForm



# Create your views here.

def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')



def form(request):
    form = PersonForm()

    if request.method == 'POST':
        # # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        # user = User.objects.create_user(last_name=last_name,email=email)
        # user.save()
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    context = {'form': form}
    return render(request, 'form.html', context)

def success(request):
    return render(request, 'success.html')



# def form(request):
#     if request.method== 'POST':
#         username=request.POST['username']
#           first_name = request.POST['first_name']
#           last_name = request.POST['last_name']
#           email = request.POST['email']
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"Username Taken")
#                 return redirect('form')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"Email Taken")
#                 return redirect('form')
#             else:
#                 user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
#                 user.save()
#                 return redirect('detail')
#         else:
#             messages.info(request,"password not matching")
#             return redirect('form')
#         return redirect('/')
#     return render(request,"form.html")
#
# def detail(request):
#     return render(request,"detail.html")




