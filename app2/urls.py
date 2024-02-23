from django.urls import path
from . import views
app_name='app2'
urlpatterns = [
path('app2home1', views.homeapp2, name="app2home1"),
path('app2hometwo', views.homeapp2two, name="app2hometwo"),
]
