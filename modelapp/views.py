from django.shortcuts import render
from modelapp import models
from django.views.generic import ListView,DetailView
# Create your views here.
class Index(ListView):
    model=models.Question
    template_name='modelapp/index.html'
    context_object_name='question_list'
class Question(DetailView):
    model=models.Question
    template_name='modelapp/question.html'