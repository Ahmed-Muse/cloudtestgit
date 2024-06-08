from django.shortcuts import render


# Create your views here.
def allifmaalUIHome(request):
  
    title="Home - Pending Tasks"
  
    context={
        "title":title,
       
    }
    return render(request,'allifmaaluiapp/home/home.html',context)

def allifmaalUIMainDashboard(request):
 
    title="Main Dashboard"
   
    context={
        "title":title,
      
    }
    return render(request,'allifmaaluiapp/dashboards/allifmaal-ui-main-dashboard.html',context)

def allifmaalUIFullSingleTable(request):
    title="Full Single Table"
   
    context={
        "title":title,
       
    }
    return render(request,'allifmaaluiapp/tables/fullsingletable.html',context)
def allifmaalUIFullTables(request):
    title="Full Single Table"
   
    context={
        "title":title,
        
    }
    return render(request,'allifmaaluiapp/tables/fulltables.html',context)

def allifmaalUIHalfTable(request):
    title="Full Single Table"
   
    context={
        "title":title,
        
    }
    return render(request,'allifmaaluiapp/tables/halftable.html',context)
def allifmaalUIHalfTables(request):
    title="Full Single Table"
   
    context={
        "title":title,
       
    }
    return render(request,'allifmaaluiapp/tables/halftables.html',context)


def allifmaalUIDetailsTable(request):
    title="Full Single Table"
   
    context={
        "title":title,
       
    }
    return render(request,'allifmaaluiapp/tables/details-table.html',context)

def allifmaalUIFormsTable(request):
    title="Full Single Table"
    
    context={
        "title":title,
       
    }
    return render(request,'allifmaaluiapp/tables/forms-table.html',context)

def allifmaalUITabs(request):
    title="Full Single Table"
    
    context={
        "title":title,
       
    }
    return render(request,'allifmaaluiapp/tables/tabs.html',context)
def allifmaalUISearch(request):
    title="Full Single Table"
    
    context={
        "title":title,
       
    }
    return render(request,'allifmaaluiapp/tables/search.html',context)



def allifmaalUIHomeFull(request):
    context={}
    return render(request,'allifmaaluiapp/uihome.html',context)

def allifmaalUIFullTable(request):
    title="Full Table"
   
    context={
        "title":title,
       
    }
    return render(request,'allifmaaluiapp/tables/fulltable.html',context)
def allifmaalUISmallTable(request):
    context={}
    return render(request,'allifmaaluiapp/tables/smalltable.html',context)

def allifmaalUI2Tables(request):
    context={}
    return render(request,'allifmaaluiapp/tables/twosmalltable.html',context)
