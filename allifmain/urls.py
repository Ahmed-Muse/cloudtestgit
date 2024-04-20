from django.contrib import admin
from django.urls import path, include
import django

#start of images 
from django.conf import settings#for uploading files
from django.conf.urls.static import static
#end of images

urlpatterns = [
    path('admin/', admin.site.urls),# uncomment after migrations
    
      path('allifmaal-erp/subscriptions/', include('allifapp.urls')),

   
    path('', include('allifmaalusersapp.urls')),
    path('Allifmaal/Application/Users/Login/App/Managers/', include('allifmaalloginapp.urls')),
    
    
   
]

    
    
    
    
    
if settings.DEBUG:#if debug which is in development stage only, then add the path below
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#this will enable 