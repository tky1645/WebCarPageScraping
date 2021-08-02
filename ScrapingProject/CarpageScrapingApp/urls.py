from django.contrib import admin
from django.urls import path,include
from .views import test_func

urlpatterns = [
    path('app/', test_func)

]
