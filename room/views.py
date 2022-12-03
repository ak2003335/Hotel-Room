from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout,login
from .models import *


def index(request):
    return render(request,'index.html')

def login(request):
    error=""
    if request.method=="POST":
        u = request.POST['uname']
        p = request.POST['pswd']
        user = auth.authenticate(username=u,password=p)
        try:
            if user.is_staff:
                auth.login(request,user)
                error="no"
            elif user is not None:
                error="not"
                auth.login(request,user)
                return redirect('user_home')
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'login.html',d)

def signup(request):
    error = ""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pwd']
        gen = request.POST['gender']
        i=request.FILES['image']
        d=request.POST['dob']
        a=request.POST['add']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Signup.objects.create(user=user,mobile=con,gender=gen,image=i,dob=d,address=a)
            error="no"
        except:
            error="yes"
    di={'error':error}
    return render(request,'signup.html',di)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'user_home.html')


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'admin_home.html')


def Logout(request):
    logout(request)
    return redirect('login')

def view_user(request):
    data = Signup.objects.all()
    d = {'data':data}
    return render(request,'view_user.html',d)


def delete_user(request,id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect('view_user')

def add_room(request):
    error=""
    if request.method=='POST':
        r=request.POST['roomno']
        p=request.POST['price']
        t=request.POST['rtype']
        s=request.POST['status']
        i=request.FILES['image']
        try:
            room.objects.create(room_no=r,price=p,r_type=t,r_status=s,r_image=i)
            error="no"
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_room.html',d)

def view_room_user(request):
    data = room.objects.all()
    d={'data':data}
    return render(request,'view_room_user.html',d)


def view_room_admin(request):
    data = room.objects.all()
    d = {'data':data}
    return render(request,'view_room_admin.html',d)

def edit_room(request):
    return render(request,'edit_room.html')
def info(request):
    error=""
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        try:
            ajeetdb.objects.create(fname=f,lname=l)
            error="no"
        except:
            error='yes'
    d = {'error': error}
    return  render(request,'ajeet.html',d)


