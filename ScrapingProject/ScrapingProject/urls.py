from django.urls import path
from django.contrib import admin
from . import views
from .views import test
 
urlpatterns = [
    #path('', views.index, name='index'),
    path ('admin/',admin.site.urls),
    path ('test/',test),
]  