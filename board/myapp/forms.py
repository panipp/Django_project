from django import forms
from .models import News,Board,Exam
from django.utils.translation import gettext_lazy as _
from django.forms import DateTimeField

class DateInput(forms.DateInput):
    input_type = 'date'

class ChoiceInput(forms.ChoiceField):
    choice_type = 'category'

class AddNewsForm(forms.ModelForm):
    title = News('title')
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'autocomplete':'off'}),input_formats=['%Y-%m-%d'])
    class Meta:
        model = News
        
        widget = {
            'date' : DateInput(),
            
        }
        labels = {
            "title" : _("หัวข้อ  "),
            "date" : _("วันที่  "),
            "file" : _("เอกสารแนบ"),
        }
        fields = ['title','date','file']
        
class AddBoard(forms.ModelForm):
    titleboard = Board('titleboard')
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'autocomplete':'off'}),input_formats=['%Y-%m-%d'])
    class Meta:
        model = Board
        widget = {
            'date' : DateInput(),
            
        }
        labels = {
            "titleboard" : _("หัวข้อ  "),
            "date" : _("วันที่  "),
            "detail" : _("คำอธิบาย "),
            "image" : _("รูปภาพ "),
        }
        fields = ['titleboard','detail','image','date']

class AddExamForm(forms.ModelForm):
    # subject = forms.ChoiceField(choices=Exam.CATEGORY_CHOICES)
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'autocomplete':'off'}),input_formats=['%Y-%m-%d'])
    class Meta:
        model = Exam
        widget = {
            'date' : DateInput(),
            
        }
        
        labels = {
            "titleexam" : _("หัวข้อ  "),
            "link" : _("link "),
            "date" : _("วันที่  "),
            "category" : _("หมวดวิชา  "),
        }
        
        fields = ['titleexam','link','date',]
