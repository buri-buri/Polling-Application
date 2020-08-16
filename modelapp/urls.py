from django.urls import path
from modelapp import views

urlpatterns=[
    path('index',views.Index.as_view(),name='index'),
    path('question/<int:pk>',views.Question.as_view(),name='question'),
]