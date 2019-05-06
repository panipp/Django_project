from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import User,Exam,News,Board
from django.template import loader
from django.views import generic
from django.urls import reverse
from .forms import AddNewsForm,AddExamForm,AddBoard

# Create your views here.
def home(request):
    # pylint: disable=no-member
    news = News.objects.all().order_by('-date')
    return render(request,'home.html',{'news' : news})

def activity(request):
    # pylint: disable=no-member
    board = Board.objects.all().order_by('-date')
    return render(request,'activity.html',{'board' : board})


def exam(request):
    # pylint: disable=no-member
    exam = Exam.objects.all()

    return render(request,'exam.html',{'exam':exam})

def news(request,**kwargs):
     # pylint: disable=no-member
    pk = kwargs['pk']
    news = News.objects.get(pk=pk)
    return render(request,'news.html',{'news': news })

def activity2(request,**kwargs):
    pk = kwargs['pk']
    activity2 = Board.objects.get(pk=pk)
    return render(request,'activity2.html',{'activity2' : activity2})

def english(request,):
    english = Exam.objects.all().order_by('-date')
    return render(request,'english.html',{'english':english})

def math(request):
    math = Exam.objects.all().order_by('-date')
    return render(request,'math.html',{'math' : math})

def others(request):
    others = Exam.objects.all().order_by('-date')
    return render(request,'others.html',{'others' : others})

def homeS(request):
    news = News.objects.all().order_by('-date')
    return render(request,'staff/homeS.html',{'news':news})

def activityS(request):
    activity = Board.objects.all().order_by('-date')
    return render(request,'staff/activityS.html',{'activity' : activity})

def examS(request):
    exam = Exam.objects.all()
    return render(request,'staff/examS.html',{'exam':exam})

def englishS(request):
    exam = Exam.objects.all()
    return render(request,'staff/englishS.html',{'exam':exam})

def mathS(request):
    exam = Exam.objects.all()
    return render(request,'staff/mathS.html',{'exam':exam})

def othersS(request):
    exam =Exam.objects.all()
    return render(request,'staff/othersS.html',{'exam':exam})

def addNews(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST,request.FILES)
        if form.is_valid():
            #save to db
            return redirect('addNews')
    else:
        form = AddNewsForm()
    return render(request,'staff/addNews.html',{'form' : form})

def addNews_summit(request):
    title = request.POST["title"]
    # file = request.POST["file"]
    date = request.POST["date"]
    news = News(title=title,date=date)
    news.save()
    return render(request,'staff/addNews.html')

# def get_title(request):
#     if request.method == 'POST':
#         form = AddNewsForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')

#     else:
#         form = AddNewsForm()
#     return render(request,'staff/addNews.html',{'form' : form})

def updateNews(request):
    return render(request,'staff/update_news.html')

def addActivity(request):
    activity = Board.objects.all()
    if request.method == 'POST':
        form = AddBoard(request.POST,request.FILES)
        if form.is_valid():
            #save to db
            return redirect('addActivity')
    else:
        form = AddBoard()
    return render(request,'staff/addActivity.html',{'form':form})

def addActivity_summit(request):
    titleboard = request.POST["titleboard"]
    # date = request.POST['date']
    detail = request.POST["detail"]
    # image = request.POST["image"]
    board = Board(titleboard=titleboard,detail=detail)
    board.save()
    return render(request,'staff/addActivity.html')    

def updateActivity(request):
    return render(request,'staff/update_activity.html')

def addExam(request):
    if request.method == 'POST':
        form = AddExamForm(request.POST,request.FILES,request.CHOICE)
        if form.is_valid():
            #save to db
            return redirect('addExam')
    else:
        form = AddExamForm()
    return render(request,'staff/addExam.html',{'form':form})

def addExam_summit(request):
    titleexam = request.POST["titleexam"]
    link = request.POST["link"]
    date = request.POST["date"]
    # category = request.POST["category"]
    exam = Exam(titleexam=titleexam,link=link,date=date)
    exam.save()
    return render(request,'staff/addExam.html')