from django.contrib import admin
from .models import *

admin.site.register(EmployeesModel)
admin.site.register(CompanyDetailsModel)
admin.site.register(CustomersModel)
admin.site.register(QuotesModel)
admin.site.register(QuoteItemsModel)

admin.site.register(SectorsModel)

admin.site.register(Category)
admin.site.register(Product)