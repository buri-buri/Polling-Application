from django.contrib import admin
from django.urls import path,include
from authapp import urls
from modelapp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authapp.urls')),
    path('questions/',include('modelapp.urls')),
]
