from django.contrib import admin
from .models import    Profiles,Exam,News,Board
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in News._meta.fields]

class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Profiles._meta.fields]

class BoardAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Board._meta.fields]

class ExamAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Exam._meta.fields]

admin.site.register(News,NewsAdmin)
admin.site.register(Board,BoardAdmin)
admin.site.register(Profiles,ProfileAdmin)
admin.site.register(Exam,ExamAdmin)