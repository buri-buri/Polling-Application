from django import forms
from modelapp import models

class AnswerForm(forms.ModelForm):
    class Meta:
        model=models.Answer
        fields=['choice']