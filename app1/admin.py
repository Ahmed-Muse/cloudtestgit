from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MyModel)
admin.site.register(MyCustomersModel)
admin.site.register(CompanyStaffModel)
admin.site.register(SuppliersModel)