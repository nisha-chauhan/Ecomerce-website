from django.shortcuts import render,redirect
from django.http import HttpResponse
from urllib import request
from django.views import View
from.models import Product
from itertools import count
from .forms import CustomerRegistrationForm,CustomerProfileForm,MyPasswordChangeForm
from django.contrib import messages
from .models import Customer 

# Create your views here.
def home(request):
    return render(request,'app/home.html',{})

def about(request):
    return render(request,'app/about.html',{})

def contact(request):
    return render(request,'app/contact.html',{})

class CategoryView(View):
    def get(self,request,val): # we add value here 
        product=Product.objects.filter(category=val)
        title=product.values('title')
        return render(request,'app/category.html',locals()) # we pass this val in the local fuction 
    
     
class CategoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request,'app/category.html',locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',locals())
    
    
class CustomerRegistratuonView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return  redirect("customerregistration")
    

class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',locals())

    def post(self,request):
        form=CustomerProfileForm(request.POST)  #form ka object
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            
            reg=Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile save successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return  redirect("profile")
    
    
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm( instance=add)
        
        return render(request,'app/updateAddress.html',locals())
    
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations! Profile save successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect("address")