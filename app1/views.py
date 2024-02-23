from django.shortcuts import render,HttpResponse,redirect
from .myforms import *

# Create your views here.

#inventory per category
def home(request):
    myobj=MyModel.objects.all()
    print(request.user)
    
   
    title="Home"
    form=MyForm1()
    if request.method == 'POST':
        form = MyForm1(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            #name=form.cleaned_data['name']
            name=request.POST.get('name')
            myname=MyModel.objects.filter(name=name).first()
            
           
            if myname !=None:
                return redirect('app1:myfunction',name=myname.id)#just redirection page
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

    }
    return render(request,'app1/home.html',context)
    
    

from django.core.mail import send_mail
def customers(request):
    
    
    custs=MyCustomersModel.objects.all()
    print(custs.explain())
    print(item for item in MyCustomersModel.objects.all())
    return render(request,'app1/customers.html',context={"customers":custs,})

def payments(request):
    return render(request,'app1/payments.html',context={})

def myfunction(request,name):
    myid=name
    
    customers=MyCustomersModel.objects.filter(owner=name)
    for item in customers:
        print(item)
    context={
        "customers":customers

    }
    
    return render(request,'app1/related.html',context)
 
    return HttpResponse("hhd")
