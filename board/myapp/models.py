from django.db import models
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    role = models.CharField(max_length = 1)

class News(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    file = models.FileField(blank = True)
    # detail = models.TextField(max_length = 300 , blank = True, null = True)


class Board(models.Model):
    titleboard = models.CharField(max_length = 500,blank=True)
    detail = models.TextField(max_length = 5000, null=True,blank=True) 
    image = models.ImageField() 
    date = models.DateField(null=True)

class Exam(models.Model):
    titleexam = models.CharField(max_length = 500,null=True)
    CATEGORY_CHOICES = (('ENG','English'),('MATH','Math'),('OTHERS','Others'))
    date = models.DateField()
    category = models.CharField(max_length=10,choices=CATEGORY_CHOICES,default='OTHERS')
    link = models.CharField(max_length = 200,null=False)

# class category(models.Model):
#     choic = models.ForeignKey(Exam,on_delete=models.CASCADE)
#     catalog = models.CharField(max_length=10,null=True)

