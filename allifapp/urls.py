from django.urls import path
from . import views
app_name='allifapp'
urlpatterns = [
    
path('Allifmaal/Main/Decision/Making/Point/Page/', views.AllifmaalDecisionPoint, name="AllifmaalDecisionPoint"),
path('Home/Main/Landing/Page/<slug:allifslug>/', views.allifappMainHome, name="allifappMainHome"),
path('Admin/Main/Home/Main/Landing/Page/Control/<slug:allifslug>/', views.allifappAdminHome, name="allifappAdminHome"),
path('Dashboard/For/Subcribers/<slug:allifslug>/', views.allifappSubsDashboard, name="allifappSubsDashboard"),


path('Employees/Staff/List/<slug:allifslug>/', views.companyEmployees, name="companyEmployees"),
path('Add/New/Employee/Staff/<slug:allifslug>/', views.addNewEmployee, name="addNewEmployee"),
path('Add/New/Company/Registration/Details/<slug:allifslug>/', views.newCompanyRegistration, name="newCompanyRegistration"),

path('Add/New/Employee/Staff/List/To/Employees/List/<slug:allifslug>/', views.addUserBySubscriberAdmin, name="addUserBySubscriberAdmin"),



path('add/customers/register/<slug:slug>/', views.addCustomer, name="addCustomer"),
path('Quotations/list/<slug:slug>/', views.quotations, name="quotations"),
path('Quotations/add/quotes/register/<slug:slug>/', views.addShowQuotes, name="addShowQuotes"),
path('Quote/add/quotes/items/register/<slug:slug>/', views.AddQuoteItems, name="AddQuoteItems"),
path('Quote/add/quotes/Details/register/<slug:slug>/', views.addQuoteDetails, name="addQuoteDetails"),

path('Form/Modifications/Quote/add/quotes/Details/register/<slug:slug>/', views.AllifQuoteDetails, name="AllifQuoteDetails"),


path('error_page/fsf/<str:message>/', views.error_page, name="error_page"),
  
path('Reset/Stff/Emplys/System/Access/ERP-subscribers/', views.Allifmaal_E_R_P_Subscribers, name="Allifmaal_E_R_P_Subscribers"),

 
path('Customers/Main/List/<str:loggedUsr>/<str:slug>/', views.customers, name="customers"),
path('Customer/Details/More/Information/About/Customer/<str:slug>/', views.CustomerDetails, name="CustomerDetails"),
path('Delete/This/Customer/Records/Permanently/<str:slug>/', views.deleteCustomer, name="deleteCustomer"),
path('Edit/Update/This/Customer/Records/Permanently/<str:slug>/', views.editCustomerDetails, name="editCustomerDetails"),

path('Customer/Dynamic/Search/allif/app/', views.CustomerCommonDynamicsearch, name="CustomerCommonDynamicsearch"),

path('for/test/again/Customer/Dynamic/Search/allif/app/', views.new_product, name="new_product"),
 
 

 path('category/for/test/again/Customer/Dynamic/Search/allif/app/', views.new_cat, name="new_cat"),
 path('formsetsfactorymodes/category/for/test/again/Customer/Dynamic/Search/allif/app/', views.edit_all_products, name="edit_all_products"),
 
path('Registered/System/Users/', views.registeredSystemUsers, name="registeredSystemUsers"),
path('Registered/System/Users/Details/View/<slug:allifslg>/', views.registeredSystemUserDetails, name="registeredSystemUserDetails"),


 
 
]   
