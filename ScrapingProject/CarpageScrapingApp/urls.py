from django.contrib import admin
from django.urls import path,include
from .views import test_func
from .BikeScrapingPackage.bikeScraping  import ExecScraping

urlpatterns = [
    path('app/', test_func),
    path('scp/', ExecScraping)
]
