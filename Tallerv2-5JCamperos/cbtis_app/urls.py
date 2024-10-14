from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from cbtis_app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('',views.indexvista, name='indexvista')# Corrected here
]
