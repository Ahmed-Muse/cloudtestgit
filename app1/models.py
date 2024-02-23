from django.db import models

# Create your models here.
class MyModel(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    

    def __str__(self):
        return self.name
