from django import forms
from .models import News,Board,Exam


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','date','file']

class AddBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['titleboard','detail','image','date']

class AddExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['titleexam','link','date']
