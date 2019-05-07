from django import forms
from .models import News,Board,Exam
from django.utils.translation import gettext_lazy as _
class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','date','file']

class AddBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['titleboard','detail','image','date']

class AddExamForm(forms.ModelForm):
    subject = forms.ChoiceField(choices=Exam.CATEGORY_CHOICES)
    
    class Meta:
        model = Exam
        fields = ['titleexam','link','date']
