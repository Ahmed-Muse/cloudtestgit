from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .myforms import *
from .models import *
from login.models import *
from django.contrib.auth.decorators import login_required 
# Create your views here.

#inventory per category
from django.contrib.auth import authenticate, login, get_user, logout#for login and logout- and authentication
from django.contrib.auth.models import AbstractUser,User
@login_required(login_url='login:userLoginPage')
def home(request,user):
    if request.user.is_authenticated:
        k=AllifmaalCustomUserModel.objects.all()
       
        kw=UserProfileModel.objects.all()
        userprofiles=UserProfileModel.objects.all()
        
        
        sysuser=request.user
        print(f"userrrrrrrrrrrrrr{sysuser.email,sysuser.lname}")
        
        myobj=MyModel.objects.all()
        staf=request.user
        class Title:
            def __init__(allif,pagetitle) -> None:
                allif.title=pagetitle
            
        title=Title("Home page")
        
        form=MyForm1()
        if request.method == 'POST':
            
            form = MyForm1(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
            
                #name=form.cleaned_data['name']
                usrname=request.POST.get('username')
                passwd=request.POST.get('passwrd')
                
                myname=MyModel.objects.filter(username=usrname,passwrd=passwd).first()
            
                if myname !=None:
                    myslug=myname.slug
                
                    
                    return redirect('app1:myfunction',system_user=staf.id,slug=myslug)#just redirection page
                    print(myname)
                    print("yesssssssssssss")
                else:
                
                    return redirect('app1:payments')
                    print("no much")
                
            
        
            # name=request.POST.get('name')
            #print(name)
            #if name in myobj:
                #return redirect('app1:customers')#just redirection page
            else:
                print("not valid")

        
                
                
            #return redirect('app1:customers')#just redirection page
        context={
            "title":title.title,
            "form":form,
            "sysuser":sysuser,
            "userprofiles":userprofiles,

        }
        return render(request,'app1/home.html',context)
    
    else:
            return login_required(login_url='login:loginpage')

def customers(request):
    sysuser=request.user
    
    
    custs=MyCustomersModel.objects.all()
    
    
    return render(request,'app1/customers.html',context={"customers":custs,"sysuser":sysuser,})

def payments(request):
    sysuser=request.user
    return render(request,'app1/payments.html',context={"sysuser":sysuser})

def myfunction(request,system_user,slug):
    allifquery=MyModel.objects.get(slug=slug)
    
  
  
    sysuser=request.user
    
    customers=MyCustomersModel.objects.filter(owner=allifquery)
    print(customers)
    staff=CompanyStaffModel.objects.filter(company=system_user)
    myad=CompanyStaffModel.objects.filter(rights="admin",company=system_user)
  
    
    
    context={
        "customers":customers,
        "staff":staff,
        "myad":myad,
        "sysuser":sysuser,
        "allifquery":allifquery,

    }
    
    return render(request,'app1/related.html',context)
 
    return HttpResponse("hhd")
def addShowSupplier(request,slug):
    title="Triage information"
    allifquery =MyModel.objects.get(slug=slug)
    sysuser=request.user
   
    form= AddSupplierForm()
    triageCheckup= get_object_or_404(MyModel, slug=slug)
    suppliers=SuppliersModel.objects.all().filter(company=allifquery)
    triageInfo = None
    if request.method == 'POST':
        form=AddSupplierForm(request.POST)
        if form.is_valid():
            triageInfo = form.save(commit=False)
            triageInfo.company= triageCheckup
            triageInfo.save()
           # return HttpResponse(post)
            return redirect('app1:addShowSupplier',slug=slug)#just redirection page

    mycontext={
   
            "form":form,
            "title":title,
            "allifquery":allifquery, 
            "suppliers":suppliers,
            "sysuser":sysuser,
    }
    return render(request,'app1/suppliers.html',mycontext)

def SupplierDetails(request,slug):
    title="Triage information"
    allifquery =SuppliersModel.objects.get(slug=slug)
    sysuser=request.user
   

    mycontext={
   
          
            "title":title,
            "allifquery":allifquery, 
           
            "sysuser":sysuser,
    }
    return render(request,'app1/supplier-details.html',mycontext)