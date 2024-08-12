from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.application, name="application"),
    
    path('predict', views.scan, name='scan'),
    path('vision/', views.datasets, name='datasets'),
    path('datasets/', views.intel, name='intel'),
    path('agribot', views.bot, name='bot'),
    path('desease/<int:pk>', views.view_d, name='data_x'),
   

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



