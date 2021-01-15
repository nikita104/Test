from django import  forms
from django.forms import formset_factory

from core import models


class StudentAnswerForm(forms.ModelForm):
    class Meta:
        model = models.StudentAnswer
        fields = '__all__'


