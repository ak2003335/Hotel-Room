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

def contact(request):
    error=""
    if request.method=='POST':
        n = request.POST['cname']
        pn = request.POST['cphone']
        e = request.POST['cemail']
        p = request.POST['cpurpose']
        try:
            Contact.objects.create(con_name=n,con_mobile=pn,con_email=e,con_purpose=p)
            error = "no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'contact.html',d)

def view_room_user(request):
    data = room.objects.all()
    d={'data':data}
    return render(request,'view_room_user.html',d)


def view_room_admin(request):
    data = room.objects.all()
    d = {'data':data}
    return render(request,'view_room_admin.html',d)

def edit_room(request,id):
    error=""
    if not request.user.is_authenticated:
        return redirect('login')
    data = room.objects.get(id=id)
    if request.method=='POST':
        n = request.POST['roomno']
        p = request.POST['price']
        rt = request.POST['rtype']
        s = request.POST['status']
        data.room_no = n
        data.price = p
        data.r_type = rt
        data.r_status = s
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'edit_room.html',d)


def delete_room(request,id):
    data = room.objects.get(id=id)
    data.delete()
    return redirect('view_room_admin')

def book_room(request,id):
    error=""
    data = room.objects.get(id=id)
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        con2 = request.POST['contact2']
        d = request.POST['booking_date']
        dy = request.POST['select_days']
        p = request.POST['price']
        g = request.POST['gender']
        add = request.POST['address']
        try:
            Booked.objects.create(first_name=f,last_name=l,email=e,gender=g,mobile1=con,mobile2=con2,booking_date=d,days=dy,price=p,address=add,status="Pending")
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'book_room.html',d)


def view_booking_admin(request):
    data = Booked.objects.all()
    d={'data':data}
    return render(request,'view_booking_admin.html',d)

def change_status(request):
    user = request.user
    # data = signup.objects.get(user=user)
    # d = {'data':data}
    return render(request,'change_status.html')
def aj(request):
    z=aj.objects.all()
    z1={'z':z}
    return render(request,'aj.html')




