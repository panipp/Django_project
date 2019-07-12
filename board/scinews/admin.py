from django.contrib import admin
from .models import    Profile,Exam,News,Board,CategoryExam
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in News._meta.fields]

class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Profile._meta.fields]

class BoardAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Board._meta.fields]

class CategoryExamAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CategoryExam._meta.fields]

class ExamAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Exam._meta.fields]

admin.site.register(News,NewsAdmin)
admin.site.register(Board,BoardAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(CategoryExam,CategoryExamAdmin)
admin.site.register(Exam,ExamAdmin)