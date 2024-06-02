from django.shortcuts import render
#from allifmaalapp.forms import AddAllifmaalQuoteDetailsForm,AddAllifmaalTasksForm
#from allifmaalapp.models import AllifmaalTasksModel,AllifmaalCustomersModel

# Create your views here.
def allifmaalUIHome(request):
    #form =AddAllifmaalTasksForm(request.POST or None)
    title="Home - Pending Tasks"
    #tasks=AllifmaalTasksModel.objects.all()
    context={
        "title":title,
        #"form":form,
        #"tasks":tasks,
    }
    return render(request,'allifmaaluiapp/home/home.html',context)

def allifmaalUIFullSingleTable(request):
    title="Full Single Table"
    #form=AddAllifmaalQuoteDetailsForm()
    #customers=AllifmaalCustomersModel.objects.all()
    context={
        "title":title,
        #"form":form,
        #"customers":customers,
    }
    return render(request,'allifmaaluiapp/tables/fullsingletable.html',context)


def allifmaalUIHomeFull(request):
    context={}
    return render(request,'allifmaaluiapp/uihome.html',context)

def allifmaalUIFullTable(request):
    title="Full Table"
    #form=AddAllifmaalQuoteDetailsForm()
    context={
        "title":title,
        #"form":form,
    }
    return render(request,'allifmaaluiapp/tables/fulltable.html',context)
def allifmaalUISmallTable(request):
    context={}
    return render(request,'allifmaaluiapp/tables/smalltable.html',context)

def allifmaalUI2Tables(request):
    context={}
    return render(request,'allifmaaluiapp/tables/twosmalltable.html',context)
