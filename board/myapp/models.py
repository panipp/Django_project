from django.db import models
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    is_staff = models.BooleanField(default = False)
    def __str__(self):
        return self.firstname
    

class News(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    file = models.FileField(upload_to='files/',blank = True)
    def __str__(self):
        return self.title

class Board(models.Model):
    titleboard = models.CharField(max_length = 500,blank=True)
    detail = models.TextField(max_length = 500, null=True,blank=True) 
    image = models.ImageField()
    date = models.DateField(null=True)
    def __str__(self):
        return self.titleboard

class Exam(models.Model):
    titleexam = models.CharField(max_length = 500,null=True)
    CATEGORY_CHOICES = (('ENG','English'),('MATH','Math'),('OTHERS','Others'))
    date = models.DateField()
    category = models.CharField(max_length=10,choices=CATEGORY_CHOICES,default='OTHERS')
    link = models.CharField(max_length = 200,null=False)
    def __str__(self):
        return self.titleexam

# class subject(models.Model):
#     subject = models.ForeignKey('Exam',on_delete=models.CASCADE)
#     eng = models.CharField()
