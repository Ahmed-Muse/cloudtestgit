from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.http.response import HttpResponse, JsonResponse
from django.urls import reverse
from allifmaalloginapp.models import AllifmaalUsersModel
from allifmaalusersapp.forms import CreateNewCustomUserForm

@login_required(login_url='allifmaalusersapp:userLoginPage')
def AllifmaalDecisionPoint(request):
    try:
        if request.user.is_authenticated:
            user_var=request.user
            title="Decision Making Page"
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            compemplye=EmployeesModel.objects.filter(username=user_var).first()
            sysadmin=AllifmaalUsersModel.objects.filter(email=user_var).first()
            sysadmincomp=CompanyDetailsModel.objects.filter(owner=user_var).first()
            if sysadmin!=None and sysadmincomp is None:
                return redirect('allifapp:newCompanyRegistration',allifslug="NewCompanyRegistrationPage")
            elif sysadmin!=None and sysadmincomp !=None:
                cmpslg=sysadmincomp.slug
                return redirect('allifapp:allifappAdminHome',allifslug=cmpslg)

            elif sysowner is None and compemplye is None:#means that the logged user did not create a company and does not belong to any company
                return redirect('allifapp:newCompanyRegistration',allifslug="NewCompanyRegistrationPage")
            
            elif sysowner!=None and user_var!=None:
                slg=sysowner.slug
                return redirect('allifapp:allifappMainHome',allifslug=slg)
                
            elif sysowner != None and compemplye != None:# user is both the owner/creator of the company and belongs to employees list of the company
                compslg=sysowner.slug
                return redirect('allifapp:allifappMainHome',allifslug=compslg)
            elif compemplye!=None:# if this is true, then the employee must be belonging to a company/entity
                emplye_comp=compemplye.company
            
                if emplye_comp!=None:
                    cmp_slug=emplye_comp.slug
                    return redirect('allifapp:allifappMainHome',allifslug=cmp_slug)
            else:
                context={"title":title,}
                return render(request,'allifapp/decide/decide.html',context)
            
        else:
             return login_required(login_url='allifmaalusersapp:userLoginPage')
            
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error/error.html',error_context)

@login_required(login_url='allifmaalloginapp:allifmaalUserLogin')
def allifappAdminHome(request,allifslug,*allifargs,**allifkwargs):
    try:
       
        user_var=request.user
        title="System Admin Home"
        context={"title":title,}
        return render(request,'allifapp/admin/home/adminhome.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error/error.html',error_context)
    
@login_required(login_url='allifmaalusersapp:userLoginPage')
def allifappMainHome(request,allifslug,*allifargs,**allifkwargs):
    try:
        user_var=request.user
        sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
        compemplye=EmployeesModel.objects.filter(username=user_var).first()
        title="Home"
        context={
            "title":title,
            "sysowner":sysowner,
            "compemplye":compemplye,
        }
        
        return render(request,'allifapp/home/mainhome.html',context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error/error.html',error_context)

@login_required(login_url='allifmaalusersapp:userLoginPage')
def allifappSubsDashboard(request,allifslug,*allifargs,**allifkwargs):
    try:
        user_var=request.user
        sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
        compemplye=EmployeesModel.objects.filter(username=user_var).first()
        title=str(sysowner) + " Dashboard"
        context={
            "title":title,
            "sysowner":sysowner,
            "compemplye":compemplye,
        }
        
        return render(request,'allifapp/dashboard/allifappdashboard.html',context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error/error.html',error_context)
    
@login_required(login_url='allifmaalusersapp:userLoginPage')
def newCompanyRegistration(request,allifslug,*allifargs,**allifkwargs):
    try:
        title="Create Company or Entity Details"
        user_var=request.user
        compny=CompanyDetailsModel.objects.filter(owner=user_var).first()
        #check if the company already exists
        if compny!=None:
            allif_obj=compny.slug
            return redirect('allifapp:allifappMainHome',allifslug=allif_obj)
        
        else:# if company does not exist, then create a new one
            form=AddCompanyDetailsForm()
            if request.method == 'POST':
                form=AddCompanyDetailsForm(request.POST)
                if form.is_valid():
                    sector=int(request.POST.get('sector'))
                    name=request.POST.get('company')
                    address=request.POST.get('address')
                    
                    if name and address!="":
                        sectorselec=SectorsModel.objects.get(id=sector)
                        obj = form.save(commit=False)
                        if sectorselec.name=="Subscription":
                            obj.owner = user_var
                            obj.save()
                            return redirect('allifapp:AllifmaalDecisionPoint')

                        elif sectorselec.name=="Distribution":
                            return redirect('allifmaalapp:allifmaalmaindashboard')
                        
                        else:
                            form=AddCompanyDetailsForm()
                            return redirect('allifapp:newCompanyRegistration',allifslug="NewCompany")
                            
                    else:
                        form=AddCompanyDetailsForm()
                        return redirect('allifapp:newCompanyRegistration',allifslug="NewCompany")  
                
            form=AddCompanyDetailsForm()
        context={"title":title,"form":form,}
        return render(request,'allifapp/company/newcompany.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error.html',error_context)
    
@login_required(login_url='allifmaalusersapp:userLoginPage')
def addUserBySubscriberAdmin(request,allifslug,*allifargs,**allifkwargs):
    try:
        title="New Staff User Registeration"
        user_var=request.user
        sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
        form=CreateNewCustomUserForm()
        if sysowner!=None:
            if request.method=='POST':
                form=CreateNewCustomUserForm(request.POST)
                email=request.POST.get('email')
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.usercompany=sysowner
                    obj.save()
                    newUser=User.objects.filter(email=obj).first()
                    if newUser!=None:
                        secret_key=newUser.customuserslug
                        context={"title":title,"form":form,"secret_key":secret_key,}
                        return render(request,"allifapp/users/userkey.html",context)
                    
                    else:
                        messages.info(request,f'User does not exist')
                        return redirect('allifmaalusersapp:newUserRegistration')
                else:
                    messages.info(request,f'Sorry {email} is likely taken, or passwords not match')
                        
        context={"title":title,"form":form,}
        return render(request,"allifapp/users/registernewuser.html",context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalusersapp/error/error.html',error_context)
    














def companyEmployees(request,allifslug,*allifargs,**allifkwargs):
    try:
        if request.user.is_authenticated:
            user_var=request.user
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            emplye=EmployeesModel.objects.filter(username=user_var).first()

            if sysowner!=None:# if true, it means that company exists and logged user is owner 
                employees=EmployeesModel.objects.filter(company=sysowner)
                context={
                "employees":employees,
                }
                return render(request,'allifapp/hrm/employees.html',context)
                
            elif emplye!=None:# if this is true, then the employee must be belonging to a company/entity
                company=emplye.company
                employees=EmployeesModel.objects.filter(company=company)
                context={
                "employees":employees,
                }
                return render(request,'allifapp/hrm/employees.html',context)
            else:
                return redirect('allifapp:decisionPoint',logged_user=user_var)
        
        else:
            return login_required(login_url='login:loginpage')
                
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error/error.html',error_context)

@login_required(login_url='login:loginpage')
def addNewEmployee(request,allifslug,*allifargs,**allifkwargs): # when someone logs in, they are directed to this page to create company details.
    #try:
        if request.user.is_authenticated:
            user_var=request.user
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            compemplye=EmployeesModel.objects.filter(username=user_var).first()
            for item in EmployeesModel.objects.all():
                print(f"employyyyy{item}")
                #item.delete()
            
            title="Add New Employee Details"
            form=AddNewEmployeeForm()
            if request.method == 'POST':
                form=AddNewEmployeeForm(request.POST)
                print("0000000000000")
                if form.is_valid():
                    print("111111111111")
                    if sysowner!=None:
                        slg=sysowner.slug
                        print("222222222222")
                        obj = form.save(commit=False)
                        obj.company =sysowner
                       
                        
                        obj.save()
                        return redirect('allifapp:companyEmployees',allifslug=slg)
                
                    elif compemplye!=None:
                        slg=compemplye.stffslug
                        comp=compemplye.company
                        obj = form.save(commit=False)
                        obj.company =comp
                        obj.save()
                        return redirect('allifapp:companyEmployees',allifslug=slg)
                        
                    else:
                        return redirect('allifapp:companyEmployees',allifslug=slg)
                       
                #else:
                    #return HttpResponse("not valid")company-access.html
                    #return render(request,'allifapp/error.html')
            else:
                form=AddNewEmployeeForm()

            context={
                "title":title,
                "form":form,
                }
            return render(request,'allifapp/hrm/add-employee.html',context)
        else:
            return login_required(login_url='login:loginpage')
    
    #except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error.html',error_context)
@login_required(login_url='login:loginpage')
def editEmployeeDetails(request,slug):
    try:
        if request.user.is_authenticated:
            user_var=request.user
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            compemplye=EmployeesModel.objects.filter(username=user_var).first()
            queryobj=CustomersModel.objects.filter(slug=slug).first()
            title="Update Customer Details"
            form=AddCustomerForm(instance=queryobj)
            if request.method == 'POST':
                if sysowner!=None:
                    slg=sysowner.slug
                    form=AddCustomerForm(request.POST,instance=queryobj)
                    if form.is_valid():
                        form.save()
                        return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
                
                elif compemplye!=None:
                    slg=compemplye.slug
                    form=AddCustomerForm(request.POST,instance=queryobj)
                    if form.is_valid():
                        form.save()
                        return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
                else:
                    return redirect('allifapp:decisionPoint',logged_user=user_var)
            
            context={
                "form":form,
                "title":title,
                "queryobj":queryobj,
            }
            return render(request,'allifapp/customers/add-customer.html',context)
            
        else:
            return login_required(login_url='login:loginpage')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error.html',error_context)

@login_required(login_url='login:loginpage')
def deleteEmployee(request,slug):
    try:
        if request.user.is_authenticated:
            user_var=request.user
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            compemplye=EmployeesModel.objects.filter(username=user_var).first()
           
            if sysowner!=None:
                slg=sysowner.slug
                CustomersModel.objects.get(slug=slug).delete()
                return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
               
            elif compemplye!=None:
                slg=compemplye.slug
                CustomersModel.objects.get(slug=slug).delete()
                return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
            else:
                return redirect('allifapp:decisionPoint',logged_user=user_var)
        else:
            return login_required(login_url='login:loginpage')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error.html',error_context)
    
@login_required(login_url='login:loginpage')
def ViewEmployeeDetails(request,slug): # when someone error.html logs in, they are directed to this page to create company details.
    try:
        if request.user.is_authenticated:
            customer=CustomersModel.objects.filter(slug=slug).first()
            context={"customer":customer,}
            return render(request,'allifapp/customers/customer-details.html',context)
        else:
            return login_required(login_url='login:loginpage')    
    except:
        return render(request,'allifapp/error.html')
    


def registeredSystemUsers(request):
    if request.user.is_authenticated:
        title="List of Registered Users"
        users=User.objects.all()
        allifmaalusers=AllifmaalUsersModel.objects.all()
        for user in users:
            print(f"caterorrrrrrrrrrr{user.user_category}")
        logged_user=request.user
        if logged_user!=None:
            user_cat=logged_user.user_category
            print(user_cat)
        context={
            "users":users,
            "user_cat":user_cat,
            "title":title,
            "allifmaalusers":allifmaalusers,
        }
        return render(request,'allifapp/users/users.html',context)
    else:
        return redirect('allifmaalusersapp:userLoginPage')

def registeredSystemUserDetails(request,allifslg):
    if request.user.is_authenticated:
        title="User Details"
        allifobj=User.objects.filter(customuserslug=allifslg).first()
        
        context={
            "allifobj": allifobj,
            
            "title":title,
        }
        return render(request,'allifapp/users/users-details.html',context)
    else:
        return redirect('allifmaalusersapp:userLoginPage')


@login_required(login_url='login:loginpage')
def customers(request,loggedUsr,slug):
    try:
        if request.user.is_authenticated:
            user_var=request.user
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            emplye=EmployeesModel.objects.filter(username=user_var).first()

            if sysowner!=None:# if true, it means that company exists and logged user is owner 
                customers=CustomersModel.objects.filter(company=sysowner)
                context={
                "customers":customers,
                }
                return render(request,'allifapp/customers/customers.html',context)
                
            elif emplye!=None:# if this is true, then the employee must be belonging to a company/entity
                company=emplye.company
                customers=CustomersModel.objects.filter(company=company)
                context={
                "customers":customers,
                }
                return render(request,'allifapp/customers/customers.html',context)
            else:
                return redirect('allifapp:decisionPoint',logged_user=user_var)
        
        else:
            return login_required(login_url='login:loginpage')
                
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error/error.html',error_context)

@login_required(login_url='login:loginpage')
def addCustomer(request,slug): # when someone logs in, they are directed to this page to create company details.
    #try:
        if request.user.is_authenticated:
            title="Add New Customer Details"
            user_var=request.user
            
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            compemplye=EmployeesModel.objects.filter(username=user_var).first()
            form=AddCustomerForm()

            if request.method == 'POST':
                form=AddCustomerForm(request.POST)
                if form.is_valid():
                    if sysowner!=None:
                        ownrentity=sysowner.company
                        obj = form.save(commit=False)
                        obj.owner =user_var
                        obj.company =sysowner
                        obj.save()
                        slg=sysowner.slug
                        return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
                
                    elif compemplye!=None:
                        slg=compemplye.stffslug
                        comp=compemplye.company
                        obj = form.save(commit=False)
                        obj.owner =user_var
                        obj.company =comp
                        obj.save()
                        return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
                        
                    else:
                        return redirect('allifapp:decisionPoint',logged_user=user_var)
                       
                else:
                    return render(request,'allifapp/error.html')
            else:
                form=AddCustomerForm()

            context={
                "title":title,
                "form":form,
                }
            return render(request,'allifapp/customers/add-customer.html',context)
        else:
            return login_required(login_url='login:loginpage')
    
    #except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error.html',error_context)
@login_required(login_url='login:loginpage')
def editCustomerDetails(request,slug):
    try:
        if request.user.is_authenticated:
            user_var=request.user
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            compemplye=EmployeesModel.objects.filter(username=user_var).first()
          
            queryobj=CustomersModel.objects.filter(slug=slug).first()
            title="Update Customer Details"
            form=AddCustomerForm(instance=queryobj)
            if request.method == 'POST':
                if sysowner!=None:
                    slg=sysowner.slug
                    form=AddCustomerForm(request.POST,instance=queryobj)
                    if form.is_valid():
                        form.save()
                        return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
                
                elif compemplye!=None:
                    slg=compemplye.slug
                    form=AddCustomerForm(request.POST,instance=queryobj)
                    if form.is_valid():
                        form.save()
                        return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
                else:
                    return redirect('allifapp:decisionPoint',logged_user=user_var)
            
            context={
                "form":form,
                "title":title,
                "queryobj":queryobj,
            }
            return render(request,'allifapp/customers/add-customer.html',context)
            
        else:
            return login_required(login_url='login:loginpage')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error.html',error_context)

@login_required(login_url='login:loginpage')
def deleteCustomer(request,slug):
    try:
        if request.user.is_authenticated:
            user_var=request.user
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            compemplye=EmployeesModel.objects.filter(username=user_var).first()
           
            if sysowner!=None:
                slg=sysowner.slug
                CustomersModel.objects.get(slug=slug).delete()
                return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
               
            elif compemplye!=None:
                slg=compemplye.slug
                CustomersModel.objects.get(slug=slug).delete()
                return redirect('allifapp:customers',loggedUsr=user_var,slug=slg)
            else:
                return redirect('allifapp:decisionPoint',logged_user=user_var)
        else:
            return login_required(login_url='login:loginpage')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error.html',error_context)
    
@login_required(login_url='login:loginpage')
def CustomerDetails(request,slug): # when someone logs in, they are directed to this page to create company details.
    try:
        if request.user.is_authenticated:
            customer=CustomersModel.objects.filter(slug=slug).first()
            context={"customer":customer,}
            return render(request,'allifapp/customers/customer-details.html',context)
        else:
            return login_required(login_url='login:loginpage')    
    except:
        return render(request,'allifapp/error.html')
    

def CustomerCommonDynamicsearch(request):
    try:
        if request.user.is_authenticated:
            user_var=request.user
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            emplye=EmployeesModel.objects.filter(username=user_var).first()
   
            if request.method=="GET":

                data_from_front_end=request.GET.get('search_result_key')
                
                if (data_from_front_end!=None):
                    allifquery= list(CustomersModel.objects.filter( 
                        Q(name__icontains=data_from_front_end)|
                        Q(balance__icontains=data_from_front_end),company=sysowner).values("name","id","balance","slug"))
                    return JsonResponse(allifquery, safe=False)
                else:
                    allifquery=CustomersModel.objects.all()
                    return JsonResponse(allifquery, safe=False)
    except:
        return render(request,'allifmaalapp/error.html')

#@login_required(login_url='login:loginpage')
#@decisionPoint(request,url='allifapp:decisionPoint')
def quotations(request,slug):
     #decisionPoint(logged_user=request.user)
    user_var=request.user
   
    sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
    compemplye=EmployeesModel.objects.filter(username=user_var).first()
    k=Category.objects.all()
    for item in k:
        #item.delete()
        print(item)
    
    if sysowner!=None:# if true, it means that company exists and logged user is owner 
        ownrcomp=sysowner.company
        quotes=QuotesModel.objects.filter(company=sysowner)
        context={
        "quotes":quotes,
        }
        return render(request,'allifapp/quotes/quotes.html',context)
       
    elif compemplye!=None:# if this is true, then the employee must be belonging to a company/entity
        company=compemplye.company
        quotes=QuotesModel.objects.filter(company=company)
        context={
        "quotes":quotes,
        }
        return render(request,'allifapp/quotes/quotes.html',context)
    
    else:
        return redirect('allifapp:decisionPoint',logged_user=user_var)
    
   
     
def addShowQuotes(request,slug):
    #try:
        
        user_var=request.user
        
        sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
        compemplye=EmployeesModel.objects.filter(username=user_var).first()
        
        if sysowner!=None:# if true, it means that company exists and logged user is owner
            owncomp=sysowner.company 
            last_obj=QuotesModel.objects.filter(company=sysowner).last()
            if last_obj:
                last_obj_id=last_obj.id
                last_obj_incremented=last_obj_id+1
                number= 'S/Quote/'+str(last_obj_incremented)
                
            else:
                number= 'Sales/'+str(uuid4()).split('-')[1]
            newobj=QuotesModel.objects.create(number=number,owner=user_var,company=sysowner)
            newobj.save()
            return redirect('allifapp:quotations',slug=slug)
            
        
        elif compemplye!=None:# if this is true, then the employee must be belonging to a company/entity
            comp=compemplye.company
            last_obj=QuotesModel.objects.filter(company=comp).last()
            if last_obj:
                last_obj_id=last_obj.id
                last_obj_incremented=last_obj_id+1
                number= 'S/Quote/'+str(last_obj_incremented)
                
            else:
                
                number= 'Sales/'+str(uuid4()).split('-')[1]
            newobj=QuotesModel.objects.create(number=number,owner=user_var,company=comp)
            newobj.save()
            return redirect('allifapp:quotations',slug=slug)
   
   
def addQuoteDetails(request,slug): # when someone logs in, they are directed to this page to create company details.
    try:
        if request.user.is_authenticated:
            user_var=request.user
            
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            emplye=EmployeesModel.objects.filter(username=user_var).first()
            qte=QuotesModel.objects.filter(slug=slug).first()#this is the slug of the clicked item on the tables
            title="Add Company Details"
        
            if sysowner!=None:
                class AddQuoteForm(forms.ModelForm):
                    class Meta:
                        model = QuotesModel
                        fields = ['customer']
                        widgets={'customer':forms.Select(attrs={'class':'form-control','placeholder':''}),}
                    def __init__(self,*args,**kwargs):
                        super (AddQuoteForm,self).__init__(*args,**kwargs) # populates the post
                        self.fields['customer'].queryset = CustomersModel.objects.filter(company=sysowner)
                form=AddQuoteForm(instance=qte)
            
            elif emplye!=None:
                shirkada=emplye.company
                class AddQuoteForm(forms.ModelForm):
                    class Meta:
                        model = QuotesModel
                        fields = ['customer']
                        widgets={'customer':forms.Select(attrs={'class':'form-control','placeholder':''}),}
                    def __init__(self,*args,**kwargs):
                        super (AddQuoteForm,self).__init__(*args,**kwargs) # populates the post
                        self.fields['customer'].queryset = CustomersModel.objects.filter(company=shirkada)
                form=AddQuoteForm(instance=qte)
        
            if request.method == 'POST':
                form=AddQuoteForm(request.POST,instance=qte)
                if form.is_valid():
                    form.save()
                    if sysowner!=None:
                        ownrslg=sysowner.slug
                        return redirect('allifapp:quotations',slug=ownrslg)
                    elif emplye!=None:
                        emplslg=emplye.slug
                        return redirect('allifapp:quotations',slug=emplslg)
                else:
                    return render(request,'allifmaalapp/error.html')
                
            context={
                "title":title,
                "form":form,}
            return render(request,'allifapp/quotes/add-quote-details.html',context)
        else:
            return login_required(login_url='login:loginpage')
    except:
        return render(request,'allifapp/error.html')

def AllifQuoteDetails(request,slug):
   
    title="Add Purchase Order Details"
    
    user_var=request.user
    
    sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
    compemplye=EmployeesModel.objects.filter(username=user_var).first()
    form=AddQuoteForm(request.user)
    if request.method == 'POST':
        #add_shipment_items_form=AddShippmentItemsForm(request.POST)
        form=AddQuoteForm(request.POST,request.FILES,instance=user_var)
        if form.is_valid():
            form.save()
            return redirect('allifmaalapp:AllifmaalPurchaseOrders')
    context={
        
        "form":form,
        

    }
    return render(request,'allifapp/quotes/add-quote-details.html',context)
       
def AddQuoteItems(request,slug):
    #try:
        title="Add items to the purchase order"
        Allif_PO=QuotesModel.objects.get(slug=slug)#very important to get id to go to particular shipment
        form=AddQuoteItemsForm()
        add_inv= get_object_or_404(QuotesModel, slug=slug)
        logged_user=request.user

        #po_Items = QuoteItemsModel.objects.filter(po_item_con=Allif_PO)#this line helps to
        
        add_item= None
        if request.method == 'POST':
            form=AddQuoteItemsForm(request.POST)
            if form.is_valid():
                add_item= form.save(commit=False)
                add_item.quoteconn=add_inv
                add_item.save()
            # return HttpResponse(post)
                return redirect('allifapp:AddQuoteItems',slug=slug)#just redirection page
        po_total=0
        #for items in po_Items:
            #po_total+=items.quantity*items.unitcost
        #po_new_amount=po_total
        #Allif_PO.total=po_new_amount
        #Allif_PO.save()

        context={
    
                "form":form,
                "title":title,
                "Allif_PO":Allif_PO,
                "add_inv":add_inv,
                #"po_Items":po_Items,
                "logged_user":logged_user,
        }
        return render(request,'allifapp/quotes/add-quote-items.html',context)
    #except:
        #return render(request,'allifmaalapp/error.html')
    
def Allifmaal_E_R_P_Subscribers(request):
    try:
        subscribers=CompanyDetailsModel.objects.all()
        subscriber_employees=EmployeesModel.objects.all()
        user_var=request.user
        sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
        ompemplye=EmployeesModel.objects.filter(username=user_var).first()
       
        users=User.objects.all()
        context={
            "subscribers":subscribers,
            "subscriber_employees":subscriber_employees,
           
            "users":users,

        }
        return render(request,'allifapp/subscribers/erp-subscribers.html',context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifapp/error/error.html',error_context)
    

def error_page(request, message):
    #if object.DoesNotExist:
        #return redirect(reverse('error_page', 
                            #kwargs={'message': "This object does not exist ( or something )"}))
    return render(request, 'allifapp/error/error_page.html', {'message': message})


def new_product(request):
    if request.method == 'POST':
        print(Product.objects.all())
        form = ProductForm(request.user, request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('allifapp:new_product')
            return redirect('products_list')
    else:
        form = ProductForm(request.user)
    return render(request, 'allifapp/product_form.html', {'form': form})
def new_cat(request):
    form = Categoryform()
    if request.method == 'POST':
        form = Categoryform(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('allifapp:new_product')
    
    return render(request, 'allifapp/cat_form.html', {'form': form})
from django.forms import formset_factory
from django.forms import ModelForm
from django.forms.models import modelformset_factory
def edit_all_products(request):
    ProductFormSet = modelformset_factory(Product, fields=('name', 'price', 'category'), extra=0)
    data = request.POST or None
    formset = ProductFormSet(data=data, queryset=Product.objects.filter(user=request.user))
    for form in formset:
        form.fields['category'].queryset = Category.objects.filter(user=request.user)

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('products_list')

    return render(request, 'allifapp/formset.html', {'formset': formset})

