from django.db import models
from django.template.defaultfilters import register, slugify
from uuid import uuid4

# Create your models here.
class MyModel(models.Model):# this is the company
    name=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    username=models.CharField(null=True, blank=True, max_length=100)
    passwrd=models.CharField(null=True, blank=True, max_length=100)
    
    

    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.name,self.address, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.name,self.address, self.uniqueId))#this is what generates the slug
        

        super(MyModel, self).save(*args, **kwargs)

class MyCustomersModel(models.Model):
    
    owner= models.ForeignKey(MyModel,related_name="stafsalrnmdsfds",on_delete=models.SET_NULL,null=True,blank=False)
    name= models.CharField(max_length=30,blank=False,null=True)
   
    def __str__(self):
    	return self.name

class CompanyStaffModel(models.Model):
    awood = [
    ('admin','admin'),
    ('staff', 'staff'),
    ('guest', 'guest'),
    ]
    
    company= models.ForeignKey(MyModel,related_name="stafsalrnmdsfdsdd",on_delete=models.SET_NULL,null=True,blank=False)
    name= models.CharField(max_length=30,blank=False,null=True)
    rights= models.CharField(choices=awood, default='admin', max_length=100)
   
    def __str__(self):
    	return self.name

class SuppliersModel(models.Model):
   
    company= models.ForeignKey(MyModel, max_length=100,on_delete=models.CASCADE,related_name="mycon")
    name= models.CharField(max_length=30,blank=False,null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
   
    
    def __str__(self):
        return str(self.company)
    
    def save(self, *args, **kwargs):
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.company,self.name, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.company,self.name, self.uniqueId))#this is what generates the slug
        

        super(SuppliersModel, self).save(*args, **kwargs)