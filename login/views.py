from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm

from django.contrib import messages
from .forms import *

#start of libraries for registration and login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, get_user, logout#for login and logout- and authentication
#end of libraries for registration and login


# Create your views here.
def newUserRegistration(request):
    title="New User Registeration"
    if request.user.is_authenticated:
        return redirect("app1:app1home")
    else:
        register_form=CreateUserForm()
        if request.method=='POST':
            register_form=CreateUserForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                username=register_form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ username)
                return redirect('login:userLoginPage')
    context={"title":title,"register_form":register_form,}
    return render(request,"register/register.html",context)

def userLoginPage(request):
    if request.user.is_authenticated:
        user=request.user
        return redirect("app1:app1home",user=user)
    else:
        form=AddUserDetailsForm()#nthis form is not used...normally html form is used instead in this case.
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:#if there is an authenticated user
                login(request, user)
                return redirect('app1:app1home',user=user)
            else:
                messages.info(request,'Dear '+username + ', Your username or password is incorrect!')
                form=AuthenticationForm(request)
    context={"form":form,}
    return render(request,'login/login.html',context)

def logoutpage(request):
    logout(request)#logs user out
    messages.success(request,"Successfully logged out ")
    return redirect('login:userLoginPage')






##################################################################################################################\
def newCustomUserRegistration(request):
    title="New User Registeration"
    if request.user.is_authenticated:
        return redirect("app1:app1home")
    else:
        register_form=CreateCustomUserForm()
        if request.method=='POST':
            register_form=CreateCustomUserForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                username=register_form.cleaned_data.get('username')
                
                return redirect('login:userLoginPage')
    context={"title":title,"register_form":register_form,}
    return render(request,"users/custom_user_register.html",context)

def CreateUserProfile(request):
    title="New User Registeration"
    
    form=UserProfileForm()
    if request.method=='POST':
        form=UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            #username=form.cleaned_data.get('username')
            
            return redirect('login:userLoginPage')
    context={"title":title,"form":form,}
    return render(request,"users/user_profile.html",context)

def CustomUser(request):
    form=CustomUserForm()

    context={"form":form,}
    return render(request,'users/custom_user.html',context)



#################################3





def systemUserProfile(request):
   

    mycontext={
        
    }
    return render(request,'profile/userProfile.html',mycontext)

def editProfile(request):
    title="Edit profile"
    user=request.user
    #editForm=UserChangeForm(instance=request.user)
    editForm=UserEditForm(instance=request.user)
    if request.method=='POST':
        editForm=UserEditForm(request.POST or None, instance=request.user)
        if editForm.is_valid():
            editForm.save()
           
            return redirect('app1:app1home',user=user)
    
    context={
        "title":title,
        "editForm":editForm,  
    }
    return render(request,"profile/editprofile.html",context)


def changeUserPassword(request):
    title="Edit profile"
    if request.method=='POST':
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass2==pass1:
            usr=request.user
            u = AllifmaalCustomUserModel.objects.get(email=usr)
            u.set_password(str(pass1))
            u.save()
           
        else:
            return redirect('login:changeUserPassword')
           
    
    
    context={
        "title":title,
       
    }
    return render(request,"profile/change_pass.html",context)

import datetime
from django.contrib.auth import logout

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            last_activity = request.session.get('last_activity', None)
            if last_activity:
                last_activity = datetime.datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
                if (datetime.datetime.now() - last_activity).seconds > 30: # 30 seconds = timeout duration
                    logout(request)
            request.session['last_activity'] = current_time
        response = self.get_response(request)
        return response
