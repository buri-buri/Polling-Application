from django.urls import path
from authapp import views

urlpatterns=[
    path('login',views.Login.as_view()),
    #path('logout',views.Logout.as_view())
]