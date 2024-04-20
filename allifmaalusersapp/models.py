from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from uuid import uuid4

class User(AbstractUser):# this is for creating new user... the fields are below and those from parent class
    user_level= [
    ('admin','admin'),
    ('staff', 'staff'),
    ('guest', 'guest'),
    ]
    #db_table = 'auth_user'# you may uncomment this if you get cusotmization related errors and see if will solve
    USERNAME_FIELD = 'email'
    username = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
    first_name= models.CharField(max_length=255, null=True,blank=False)
    last_name= models.CharField(max_length=255, null=True,blank=False)
    REQUIRED_FIELDS = ['username','first_name','last_name'] # removes email from REQUIRED_FIELDS
    user_category= models.CharField(choices=user_level, default='guest', max_length=100,null=True,blank=True)
    
    customuserslug= models.SlugField(max_length=500, unique=True, blank=True, null=True)
    randomfield=models.CharField(max_length=255, null=True,blank=True)
    secret_unique_id= models.CharField(null=True, blank=True, max_length=100)
    customurlslug= models.SlugField(max_length=500, unique=True, blank=True, null=True)
    url_unique_id= models.CharField(null=True, blank=True, max_length=100)
    usercompany= models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        if self.secret_unique_id is None:
            self.secret_unique_id= str(uuid4()).split('-')[4]
            self.customuserslug = slugify('{} '.format(self.secret_unique_id))
        if self.url_unique_id is None:
            self.url_unique_id=str(uuid4()).split('-')[4]
            self.customurlslug = slugify('{} {} {}'.format(self.first_name,self.last_name,self.url_unique_id))

        self.customuserslug = slugify('{}'.format(self.secret_unique_id))#this is what generates the slug
        self.customurlslug = slugify('{} {} {}'.format(self.first_name,self.last_name,self.url_unique_id))
        super(User, self).save(*args, **kwargs)
        
class UserLoginDetailsModel(models.Model):#this is for the login
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
   
    def __str__(self):
        return self.username
