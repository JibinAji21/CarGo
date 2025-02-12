from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
# from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.conf import settings

# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname    #--------------->creating session
                return redirect(shop_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"Invalid username or password")
            return redirect(shop_login)
    else:
        return render(req,'login.html')
    
def shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(shop_login)
    
    

def shop_home(req):
    if 'shop' in req.session:
        car=Cars.objects.all()
        return render(req,'shop/home.html',{'cars':car})
    else:
        return redirect(shop_login)
    

def add_car(req):
    if req.method=='POST':
        id=req.POST['car_id']
        name=req.POST['car_name']
        year=req.POST['car_year']
        place=req.POST['car_place']
        rent=req.POST['car_rent']
        fuel=req.POST['car_fuel']
        file=req.FILES['car_img']
        data=Cars.objects.create(car_id=id,car_name=name,car_year=year,car_place=place,car_rent=rent,car_fuel=fuel,car_img=file)
        data.save()
        return redirect(shop_home)
    return render(req,'shop/addcar.html')

def edit_car(req,id):
    car=Cars.objects.get(pk=id)
    if req.method=='POST':
        e_id=req.POST['car_id']
        name=req.POST['car_name']
        year=req.POST['car_year']
        place=req.POST['car_place']
        rent=req.POST['car_rent']
        fuel=req.POST['car_fuel']
        file=req.FILES.get('car_img')
        if file:
            Cars.objects.filter(pk=id).update(car_id=e_id,car_name=name,car_year=year,car_place=place,car_rent=rent,car_fuel=fuel,car_img=file)
        else:
            Cars.objects.filter(pk=id).update(product_id=e_id,product_name=name,car_year=year,car_place=place,car_rent=rent,car_fuel=fuel)
        return redirect(shop_home)
    return render(req,'shop/edit_car.html',{'data':car})

def delete_product(req,id):
    data=Cars.objects.get(pk=id)
    url=data.img.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(shop_home)


    
def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(shop_login)
        except:
            messages.warning(req,"Email Exists")
            return redirect(register)
    else:
        return render(req,'user/register.html')
    

def user_home(req):
    if 'user' in req.session:
        data=Cars.objects.all()
        return render(req,'user/customer_home.html',{'data':data})
    else:
        return redirect(shop_login)