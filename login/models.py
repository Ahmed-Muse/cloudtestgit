
# Create your models here.
from django.db import models
#from allifmaalapp.models import SystemRightsModel
from django.template.defaultfilters import register, slugify
from uuid import uuid4
# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin,
)
from django.contrib.auth import get_user_model
class UserDetailsModel(models.Model):
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    def __str__(self):
        return str(self.username)

#
#################3 update user model 5th april 2024
class UserManager(BaseUserManager):
    def create_user(self, email,fname,lname, password=None,is_staff=False,is_admin=False):# This takes all required fields
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not fname:
            raise ValueError('Users must have a first name')
        if not lname:
            raise ValueError('Users must have a last name')

        user = self.model(email=self.normalize_email(email),
        # if there are other required fields, add them here and also add as parameters to the function create_user
        fname=fname,
        lname=lname
        )

        user.set_password(password)
        user.staff=is_staff
        user.admin=is_admin
        #user.active=is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,fname,lname, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            fname=fname,
            lname=lname
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# hook in the New Manager to our Model
#class AllifmaalCustomUserModel(AbstractBaseUser): # from step 2
    #...
    #objects = UserManager()
    #class Meta:     #you have to add abstract class
        #abstract = True


class AllifmaalCustomUserModel(AbstractBaseUser):
    awood = [
    ('admin','admin'),
    ('staff', 'staff'),
    ('guest', 'guest'),
    ]
    
    email = models.EmailField(
        verbose_name='email address',default="",
        max_length=255,
        unique=True,
    )
    #is_active = models.BooleanField(default=True)
    fname=models.CharField(max_length=255, null=True)
    lname=models.CharField(max_length=255, null=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField('Mark admin',default=False) # a superuser
    category= models.CharField(choices=awood, default='staff', max_length=100)

    # notice the absence of a "Password field", that is built in.
    comments = models.CharField(max_length=255, null=True)
    #timestamp=models.DateTimeField(auto_now_add=False)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)

    USERNAME_FIELD = 'email'# this means new user login will be email now
    REQUIRED_FIELDS = ['fname','lname'] # Email & Password are required by default.
    #any field in the required fields must be added to the parameters of create_user method
    objects = UserManager()# hook in the New Manager to our Model
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return str(self.fname)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    #@property
    #def is_active(self):
        #"Is the user a admin member?"
       # return self.is_active
    
    def save(self, *args, **kwargs):
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.fname, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.fname, self.uniqueId))#this is what generates the slug
        super(AllifmaalCustomUserModel, self).save(*args, **kwargs)

# if you wish you can extend the above model information by adding profile model as below
from django.conf import settings
class UserProfileModel(models.Model):# you can have the profile for the user
    name= models.OneToOneField(AllifmaalCustomUserModel,on_delete=models.SET_NULL,null=True)# this extends functionality through inheritance
    title= models.CharField(max_length=255, null=True)

    #author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    def __str__(self):
        return self.title
    

    