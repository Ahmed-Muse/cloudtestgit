from django.db import models

# Create your models here.
class MyModel(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    

    def __str__(self):
        return self.name

class MyCustomersModel(models.Model):
    
    owner= models.ForeignKey(MyModel,related_name="stafsalrnmdsfds",on_delete=models.SET_NULL,null=True,blank=False)
    name= models.CharField(max_length=30,blank=False,null=True)
   
    def __str__(self):
    	return self.name
