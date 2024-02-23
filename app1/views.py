from django.shortcuts import render,HttpResponse

# Create your views here.

#inventory per category
def home(request):

    title="Stock Per Category And Stock Search"
    
    context={
        "title":title,

    }
    return render(request,'app1/home.html',context)
    
    


def hometwo(request):
    return HttpResponse("ddd")
