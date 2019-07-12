import json
import requests
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.core.validators import RegexValidator

from django import forms


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=1128)
    def __str__(self):
            return self.name
            
class Department(models.Model):
    name = models.CharField(max_length=128,null=True)
    faculty = models.ForeignKey(Faculty,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        if not self.faculty and self.name:
            return self.name
        if not self.name and self.faculty:
            return self.faculty
        if self.faculty and self.name:
            return "%s, %s"%(self.faculty, self.name)
        return "ไม่ระบุ"

class Role(models.Model):
    name = models.CharField(max_length=128,null=True)
    def __str__(self):
        return self.name


class Profiles(models.Model):
    account             = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    prefix_name         = models.CharField(max_length=50,null=True, help_text="example Mr.")
    name                = models.CharField(max_length=128,null=True, help_text="example James")
    mid_name            = models.CharField(max_length=128,null=True,blank=True, help_text="example Clerk")
    last_name           = models.CharField(max_length=128,null=True, help_text="example Maxwell")
    prefix_th_name      = models.CharField(max_length=50,null=True,blank=True, help_text="เช่น นาย")
    th_name             = models.CharField(max_length=128,null=True,blank=True, help_text="เช่น เจมส์")
    th_mid_name         = models.CharField(max_length=128,null=True,blank=True, help_text="เช่น เคลิร์ก")
    th_lastname         = models.CharField(max_length=128,null=True,blank=True, help_text="เช่น แมกซ์เวลล์")
    email               = models.EmailField(null=True, help_text="เช่น maxwell.james@example.com")
    table_no            = models.CharField(max_length=128,null=True,blank=True, help_text="เช่น 02-564-444-059 ต่อ 2157")
    room_no             = models.CharField(max_length=128,null=True,blank=True, help_text="เช่น บร2 ห้อง 224")
    role                = models.ForeignKey(Role,on_delete=models.SET_NULL,null=True)
    position            = models.CharField(max_length=128,null=True,blank=True, help_text="ตำแหน่งงาน")
    department          = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    phone               = models.CharField(max_length=128, blank=True, help_text="เช่น 02-564-444-059 ต่อ 2157")
    academic_profile    = models.TextField(null=True,blank=True)
    cooperative         = models.TextField(null=True,blank=True,default='')
    image               = models.ImageField(upload_to='image/',null=True,blank=True, help_text="เช่น Maxwell")
    def __str__(self):
        return self.name

class ProfilesForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfilesForm, self).__init__(*args, **kwargs)
        # self.fields['prefix_name'].widget.attrs['placeholder'] = 'Mr.'
        # self.fields["name"].widget.attrs['placeholder'] = 'Jame'
        # self.fields["mid_name"].widget.attrs['placeholder'] = 'Clerk'
        # self.fields["last_name"].widget.attrs['placeholder'] = 'Maxwell'
        # self.fields["prefix_th_name"].widget.attrs['placeholder'] = 'นาย'
        # self.fields["th_name"].widget.attrs['placeholder'] = 'เจมส์'
        # self.fields["th_mid_name"].widget.attrs['placeholder'] = 'เคลิร์ก'
        # self.fields["th_lastname"].widget.attrs['placeholder'] = 'แมกซ์เวลล์'
        # self.fields["email"].widget.attrs['placeholder'] = 'maxwell.james@example.com'
        # self.fields["table_no"].widget.attrs['placeholder'] = '02-564-444-059 ต่อ 2157'
        # self.fields["room_no"].widget.attrs['placeholder'] = 'บร2 ห้อง 224'
        # self.fields["position"].widget.attrs['placeholder'] = 'ตำแหน่งงาน'
        # self.fields["phone"].widget.attrs['placeholder'] = '02-564-444-059 ต่อ 2157'
        self.fields["academic_profile"].widget.attrs['placeholder'] = \
""" Maxwell, James Clerk. A treatise on electricity and magnetism. Vol. 1. Clarendon press, 1881.
    Maxwell, James Clerk. The Scientific Papers of James Clerk Maxwell... Vol. 2. University Press, 1890.
"""
        self.fields["cooperative"].widget.attrs['placeholder'] = "รายละเอียดการร่วมงานกับเอกชน"
    
    class Meta:
        model   = Profiles
        fields  = '__all__'
        labels  = {
            "prefix_name"       : _("Prefix"),
            "name"              : _("First Name"),
            "mid_name"          : _("Middle Name"),     
            "last_name"         : _("Last Name"),
            "prefix_th_name"    : _("คำนำหน้าไทย"),
            "th_name"           : _("ชื่อไทย"),
            "th_mid_name"       : _("ชื่อกลาง"),
            "th_lastname"       : _("นามสกุลไทย"),
            "email"             : _("Email"),
            "table_no"          : _("Office Telephone"),
            "room_no"           : _("Office Room"),
            "position"          : _("Job Position"),
            "department"        : _("Department"),
            "phone"             : _("Mobile Phone"),
            "academic_profile"  : _("Academic Profile"),
            "cooperative"       : _("Business Collaborative Profile"),
            "image"             : _("Display Image"),
        }
        exclude = ['account', "role"]

def logged_in_handle(sender, user, request, **kwargs):
    ROLE = {
        'STUDENT': '1',

    }
    #
    # Check if TU login
    prov = user.social_auth.filter(provider='tu')
    if prov.exists():
        data    = prov[0].extra_data
        headers = {
            "Authorization": "Bearer {}".format(data['access_token'])
        }
        api  = requests.get('https://api.tu.ac.th/api/me/', headers=headers).json()
        # if api['company'] == 'คณะวิทยาศาสตร์และเทคโนโลยี':
        if api['role']!='1':   #<<----THIS !!!!!
        # if api['role']=='1':    
            # print("API : ", api)
            # print("api['username'] :", api['username'])
            # print(Profiles.objects.all())
            index   = User.objects.all().filter(username = api['username'])[0]
            profile = Profiles.objects.filter(account = index)
            # print("Profile : ", profile)
            if not profile.exists():
                # print("profile not exists")
                create_init_faculty, _ = Faculty.objects.get_or_create(
                    name=api['company']
                )
                create_init_department, _ = Department.objects.get_or_create(
                    name=api['department'],
                    faculty=create_init_faculty,
                )
                create_init_profile     = Profiles.objects.create(
                    account = index,
                    department = create_init_department,
                    name    = api['firstname'],
                    last_name = api['lastname'],
                )
user_logged_in.connect(logged_in_handle)
