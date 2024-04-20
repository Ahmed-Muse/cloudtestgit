from django.db import models
from django.template.defaultfilters import register, slugify
from uuid import uuid4
#from django.contrib.auth.models import User
from allifmaalusersapp.models import User

# Create your models here.
gender = (
		('Male', 'Male'),
		('Female', 'Female'),
	)

class SectorsModel(models.Model):# this is the company  hospitality logistics
    name=models.CharField(max_length=20,blank=False,null=False,unique=True)
    notes=models.CharField(max_length=50,blank=True,null=True)
   
    def __str__(self):
        return self.name
   

class CompanyDetailsModel(models.Model):# this is the company
    company=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    pobox=models.CharField(max_length=50,blank=True,null=True)
    email=models.EmailField(max_length=50,blank=True,null=True)
    website=models.CharField(max_length=50,blank=True,null=True)
    phone1=models.CharField(max_length=50,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    country=models.CharField(max_length=50,blank=True,null=True)
    phone2=models.CharField(max_length=50,blank=True,null=True)
    logo=models.ImageField(blank=True,null=True)
    owner= models.OneToOneField(User, on_delete=models.PROTECT,blank=True,null=True)
    sector= models.ForeignKey(SectorsModel,related_name="secrlmcomp",on_delete=models.PROTECT,null=True,blank=False)
    
    def __str__(self):
        return str(self.company)
    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.company,self.address, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.company,self.address, self.uniqueId))#this is what generates the slug
        
        super(CompanyDetailsModel, self).save(*args, **kwargs)
        










        
class EmployeesModel(models.Model):
    rights= [
		('admin', 'admin'),
		('staff', 'staff'),
        ('owner', 'owner'),
        ('guest', 'guest'),
        ('manager', 'manager'),
        ('director', 'director'),
	]
    staffNo = models.IntegerField(default='0',blank=False,null=False,unique=True)
    firstName = models.CharField(max_length=50,blank=False,null=True)
    lastName = models.CharField(max_length=50,blank=False,null=True)
    middleName = models.CharField(max_length=50,blank=True,null=True)
    gender = models.CharField(max_length=25, blank=True, null=True,choices=gender)
    department = models.CharField(max_length=50,blank=True,null=True)
    title = models.CharField(max_length=50,blank=True,null=True)
    education = models.CharField(max_length=50,blank=True,null=True)
    comment = models.CharField(max_length=50,blank=True,null=True)
    dateJoined =  models.DateTimeField(auto_now_add=True,blank=True,null=True)
    #timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    salary=models.DecimalField(max_digits=10,blank=False,null=True,decimal_places=1,default=0)
    total_salary_paid=models.DecimalField(max_digits=10,blank=True,null=True,decimal_places=1,default=0)
    salary_payable=models.DecimalField(max_digits=10,blank=False,null=True,decimal_places=1,default=0)
    salary_balance=models.DecimalField(max_digits=10,blank=False,null=True,decimal_places=1,default=0)
    username= models.OneToOneField(User, on_delete=models.CASCADE)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    sysperms= models.CharField(choices=rights, blank=True, null=True,max_length=30,default="staff")
    company= models.ForeignKey(CompanyDetailsModel,related_name="emplcomprlnmefsa",on_delete=models.SET_NULL,null=True,blank=True)
    
    stffslug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    def __str__(self):
        return self.firstName
        
    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.stffslug = slugify('{} {} {} {} {}'.format(self.company,self.company.address, self.uniqueId,self.firstName,self.middleName))

        self.stffslug = slugify('{} {} {} {} {}'.format(self.company,self.company.address, self.uniqueId,self.firstName,self.middleName))#this is what generates the slug
        
        
        super(EmployeesModel, self).save(*args, **kwargs)

#####3 i customers 
class CustomersModel(models.Model):
    Country = [
    ('Somalia', 'Somalia'),
    ('Kenya', 'Kenya'),
     ('Other', 'Other'),
    ]
     
    name = models.CharField(null=True, blank=False, max_length=20)
    phone = models.CharField(null=True, blank=True, max_length=30)
    email= models.CharField(null=True, blank=True, max_length=100)
    country = models.CharField(choices=Country, blank=True, max_length=30)
    city= models.CharField(null=True, blank=True, max_length=30)
    address = models.CharField(null=True, blank=True, max_length=30)
    sales=models.DecimalField(max_digits=10,blank=False,null=True,decimal_places=1,default=0)
    balance=models.DecimalField(max_digits=10,blank=False,null=True,decimal_places=1,default=0)
    turnover=models.DecimalField(max_digits=10,blank=False,null=True,decimal_places=1,default=0)
    contact = models.CharField(null=True, blank=True, max_length=30)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    
    owner= models.ForeignKey(User,related_name="cuscmprlne",on_delete=models.SET_NULL,null=True,blank=False)
    
    company= models.ForeignKey(CompanyDetailsModel,related_name="cuscmprln",on_delete=models.SET_NULL,null=True,blank=False)
    

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))#this is what generates the slug
        

        super(CustomersModel, self).save(*args, **kwargs)
   
    

class SuppliersModel(models.Model):
    Country = [
    ('Somalia', 'Somalia'),
    
    ('Kenya', 'Kenya'),
     ('Other', 'Other'),
    ]
    name = models.CharField(null=True, blank=False, max_length=20)
    phone = models.CharField(null=True, blank=True, max_length=30)
    email= models.CharField(null=True, blank=True, max_length=100)
    country = models.CharField(choices=Country, blank=True, max_length=30)
    city= models.CharField(null=True, blank=True, max_length=30)
    address = models.CharField(null=True, blank=True, max_length=30)
    balance=models.DecimalField(max_digits=10,blank=False,null=True,decimal_places=1,default=0)
    turnover=models.DecimalField(max_digits=10,blank=False,null=True,decimal_places=1,default=0)
   
    contact = models.CharField(null=True, blank=True, max_length=30)
   
    company= models.ForeignKey(CompanyDetailsModel, max_length=100,on_delete=models.CASCADE,related_name="cmpsuprlnmes")
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
   
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))#this is what generates the slug
        

        super(SuppliersModel, self).save(*args, **kwargs)



################################3 QUOTES ###########################3
class QuotesModel(models.Model):
   
    number = models.CharField(null=True, blank=True, max_length=20)
    customer= models.ForeignKey(CustomersModel,related_name="apqotelnm",on_delete=models.SET_NULL,blank=True,null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    owner= models.ForeignKey(User,related_name="cuscmprlneqt",on_delete=models.SET_NULL,null=True,blank=True)
    
    company= models.ForeignKey(CompanyDetailsModel,related_name="cuscmprlqtn",on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return '{}'.format(self.number)
    def save(self, *args, **kwargs):
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.number, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.number, self.uniqueId))#this is what generates the slug
        
        super(QuotesModel, self).save(*args, **kwargs)
class QuoteItemsModel(models.Model):
    #description= models.ForeignKey('AllifmaalStocksMode',related_name="allifquoteitemdescrelatednm",on_delete=models.SET_NULL,blank=True,null=True)
    description= models.CharField(null=True, blank=True, max_length=20)
    quantity = models.DecimalField(max_digits=10,blank=False,null=True,decimal_places=1,default=0)
  
    quoteconn= models.ForeignKey(QuotesModel, blank=True, null=True, on_delete=models.CASCADE,related_name='allifquoteitemrelated')
    
    def __str__(self):
        return '{}'.format(self.description)
    #below calculates the total selling price for the model

class Category(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category,blank=True, null=True, on_delete=models.CASCADE,related_name='allifquoteitemrelatedfgfd')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name)