from django import forms
from .models import News,Board,Exam
from django.utils.translation import gettext_lazy as _
from django.forms import DateTimeField,FileInput

class DateInput(forms.DateInput):
    input_type = 'date'

class ChoiceInput(forms.ChoiceField):
    choice_type = 'category'

class AddNewsForm(forms.ModelForm):
    title = News('title')
    file = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}),label="เอกสารแนบ ")
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'autocomplete':'off'}),input_formats=['%Y-%m-%d'],label="วันที่ ")
    class Meta:
        model = News
        
        widget = {
            'date' : DateInput(),
        }
        labels = {
            "title" : _("หัวข้อ  "),
        }
        fields = ['title','date','file']
        
class AddBoard(forms.ModelForm):
    titleboard = Board('titleboard')
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'autocomplete':'off'}),input_formats=['%Y-%m-%d'],label="วันที่ ")
    image = forms.ImageField(widget=forms.FileInput(),label="รูปภาพ ")
    class Meta:
        model = Board
        widget = {
            'date' : DateInput(),
            
        }
        labels = {
            "titleboard" : _("หัวข้อ  "),
            "detail" : _("คำอธิบาย "),
        }
        fields = ['titleboard','date','detail','image']

class AddExamForm(forms.ModelForm):
    # subject = forms.ChoiceField(choices=Exam.CATEGORY_CHOICES)
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'autocomplete':'off'}),input_formats=['%Y-%m-%d'],label="วันที่ ")
    class Meta:
        model = Exam
        widget = {
            'date' : DateInput(),
            
        }
        
        labels = {
            "titleexam" : _("หัวข้อ  "),
            "link" : _("ลิ้งค์ "),
            "category" : _("หมวดวิชา  "),
        }
        
        fields = ['titleexam','date','link','category']
