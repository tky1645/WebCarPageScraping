from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('CarpageScrapingApp/', include('CarpageScrapingApp.urls')),
    path('admin/', admin.site.urls),
]