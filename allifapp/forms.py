from django import forms
from .models import *



############################# start of datepicker customization ##############################
class DatePickerInput(forms.DateInput):#use this class whereever you have a date and it will give you the calender
    input_type = 'date'#
class TimePickerInput(forms.TimeInput):#use this wherever you have time input
    input_type = 'time'
class DateTimePickerInput(forms.DateTimeInput):#use this wherever you have datetime input
    input_type = 'datetime'
    ################################# end of datepicker customization ################################


class AddCompanyDetailsForm(forms.ModelForm):
    class Meta:
        model = CompanyDetailsModel
        fields = ['company','sector','owner','phone1','email','website', 'logo','address','phone2','pobox','city','country']
        widgets={
            'company':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            #'username':forms.TextInput(attrs={'class':'form-control','placeholder':''}),

            'phone1':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'owner':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'sector':forms.Select(attrs={'class':'form-control','placeholder':''}),
            
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'pobox':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'phone2':forms.TextInput(attrs={'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
            #'logo':forms.ImageField(attrs={'class':'form-control'}),
             #'passwrd':forms.TextInput(attrs={'class':'form-control','type':'password'}),
        
        }
    def __init__(self,*args,**kwargs):
        #assets_queryset=AllifmaalChartOfAccountsModel.objects.filter(code__lte=19999)
        super().__init__(*args,**kwargs)
        #self.fields['owner']="Details"
        
    

        #super().__init__(*args, **kwargs)
    #def form_valid(self,AddCompanyDetailsForm):
        #AddCompanyDetailsForm.instance.owner = self.request.user
        
      
        
        #self.fields['owner'].queryset=u


class AddNewEmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeesModel
        fields = ['staffNo','firstName','lastName','middleName','gender','department','title','education',
                  'comment','salary','total_salary_paid','salary_payable','salary_balance','username','sysperms','company']
        widgets={
            'staffNo':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'firstName':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'lastName':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'middleName':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'education':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'comment':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'salary':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'total_salary_paid':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'salary_payable':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'salary_balance':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'username':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'sysperms':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'company':forms.Select(attrs={'class':'form-control','placeholder':''}),

            
        }






class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = CustomersModel
        fields = ['name','phone','email','country','phone','email','city', 'address','sales']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':''}),

            'email':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
           
            
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
           
        
        }


class AddQuoteForm(forms.ModelForm):

    class Meta:
        model = QuotesModel
        fields = ['customer','owner','company']
        widgets={
            'customer':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'company':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'owner':forms.Select(attrs={'class':'form-control','placeholder':''}),
        }
        def __init__(self, user, *args, **kwargs):
            super(AddQuoteForm, self).__init__(*args, **kwargs)
            self.fields['customer'].queryset = CustomersModel.objects.filter(customer=user)
    #def __init__(self,company,*args,**kwargs):
        #super (AddQuoteForm,self ).__init__(*args,**kwargs) # populates the post
        #self.fields['company'].queryset = CompanyDetailsModel.objects.filter(company=company)
        #self.fields['customer'].queryset = CustomersModel.objects.filter(company=company)

    #def __init__(self, *args, **kwargs):
        #super(AddQuoteForm, self).__init__(*args, **kwargs)
        #if self.instance:
            #self.fields['customer'].queryset =CustomersModel.objects.filter(company=self.instance)
        
    #def __init__(self,*args,**kwargs):
        
        #allifqueryset=CustomersModel.objects.filter(company=user_var)
        #form = super(QuotesModel, self).get_form(*args, **kwargs)

        #super().__init__(*args, **kwargs)
        
        #self.fields['customer'].queryset=CustomersModel.objects.filter(company=self.request.user.company)
        #form.rate.queryset = Rate.objects.filter(company_id=the_company.id)
    #def get_form(self, *args, **kwargs):
        #form = super(QuotesModel, self).get_form(*args, **kwargs)
        #kk=self.request.user

        #form.fields['customer'].queryset = CustomersModel.objects.filter(company=self.request.user.company)
        # form.fields['b_a'].queryset = A.objects.filter(a_user=self.request.user)
        #print(f"11111111111111111{kk}") 
        #return form
    #def __init__(self, *args, user, **kwargs):
        #self.user = user
        #super().__init__(*args, **kwargs)
        #self.fields['customer'].queryset =CustomersModel.objects.filter(owner=self.user)
    
class AddQuoteItemsForm(forms.ModelForm):
    class Meta:
        model = QuoteItemsModel
        fields = ['description','quantity']
        widgets={
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'quantity':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            
           
        
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'category', )
        widgets={
            #'company':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
             'price':forms.TextInput(attrs={'class':'form-control','placeholder':''}),

          
            #'owner':forms.Select(attrs={'class':'form-control','placeholder':''}),
           
             'category':forms.Select(attrs={'class':'form-control'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','user']
        widgets={
            #'company':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':''}),

          
            #'owner':forms.Select(attrs={'class':'form-control','placeholder':''}),
           
             'user':forms.Select(attrs={'class':'form-control'}),
        
        }