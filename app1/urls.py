from django.urls import path
from . import views
from uuid import uuid4

def ouruser(request):
    global syus
    syus=request.user
    return syus


appref= '17086#&ERP'+str(uuid4()).split('-')[1]
app_name='app1'
urlpatterns = [
path('ourhome/<str:user>/', views.home, name="app1home"),
path('customers', views.customers, name="customers"),
path('payments', views.payments, name="payments"),
path(f'Allifmaal-ERP/erp45ems1912<str:system_user>{appref}<slug:slug>/', views.myfunction, name="myfunction"),
path('Add-supplier-Details/<slug:slug>/', views.addShowSupplier, name="addShowSupplier"),

path('supplier-Details/<slug:slug>/', views.SupplierDetails, name="SupplierDetails"),


]
