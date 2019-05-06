from django.contrib import admin
from .models import    User,Exam,News,Board
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_news = ('title','date','detail','file',)

class UserAdmin(admin.ModelAdmin):
    list_user = ('firstname','lastname','role',)

class BoardAdmin(admin.ModelAdmin):
    list_board = ('titleboard','detail','image' , 'date',)

class ExamAdmin(admin.ModelAdmin):
    list_exam = ('titleexam','date','category','link',)

admin.site.register(News,NewsAdmin)
admin.site.register(Board,BoardAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Exam,ExamAdmin)

