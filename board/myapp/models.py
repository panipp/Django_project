import requests, json
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.http import HttpResponseForbidden
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError


# Create your models here.
class Profiles(models.Model):
    account = models.OneToOneField(User, on_delete = models.PROTECT)
    company = models.CharField(max_length=128,null=True)
    department = models.CharField(max_length=128,null=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(null=True, help_text="เช่น somename@example.com")

    is_staff = models.BooleanField(default = False)
    def __str__(self):
        return self.account.username

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

def logged_in_handle(sender, user, request, **kwargs):
    if request.user.is_superuser:
        return None

    prov = user.social_auth.filter(provider='tu')
    if prov.exists():
        data    = prov[0].extra_data
        headers = {
            "Authorization": "Bearer {}".format(data['access_token'])
        }
        api  = requests.get('https://api.tu.ac.th/api/me/', headers=headers).json()

        index   = User.objects.all().filter(username = api['username'])[0]
        profile = Profiles.objects.filter(account = index)
        
        if not profile.exists():
            Profiles.objects.create(
                account = index,
                company = api['company'],
                department = api['department'],
                firstname = api['firstname'],
                lastname = api['lastname'],
                email = api['tumail'],
            )
user_logged_in.connect(logged_in_handle)
