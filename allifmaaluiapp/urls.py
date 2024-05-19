from django.urls import path
from . import views
app_name='allifmaaluiapp'
urlpatterns = [
path('UI/Home/', views.allifmaalUIHome, name="allifmaalUIHome"),#this is the home page
path('UI/Home/Full/Table/', views.allifmaalUIFullTable, name="allifmaalUIFullTable"),

path('UI/Home/Full/Half/Table/', views.allifmaalUISmallTable, name="allifmaalUISmallTable"),
path('UI/Home/Two/Small/Table/', views.allifmaalUI2Tables, name="allifmaalUI2Tables"),

   
]  