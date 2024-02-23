from django.urls import path
from . import views
app_name='app1'
urlpatterns = [
path('', views.home, name="app1home"),
path('customers', views.customers, name="customers"),
path('payments', views.payments, name="payments"),
path('Allifmaal-ERP@67<str:name>325$#allifmaal', views.myfunction, name="myfunction"),


]
