from django.shortcuts import render

# Create your views here.
def allifmaalUIHome(request):
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
