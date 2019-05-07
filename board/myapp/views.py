from django.shortcuts import render,redirect,get_object_or_404
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
    exams = Exam.objects.all()

    return render(request,'exam.html',{'exams':exams})

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
    englishs = Exam.objects.all().order_by('-date')
    return render(request,'english.html',{'englishs':englishs})

def math(request):
    maths = Exam.objects.all().order_by('-date')
    return render(request,'math.html',{'maths' : maths})

def others(request):
    otherss = Exam.objects.all().order_by('-date')
    return render(request,'others.html',{'otherss' : otherss})

def homeS(request):
    news = News.objects.all().order_by('-date')
    return render(request,'staff/homeS.html',{'news':news})

def activityS(request):
    activity = Board.objects.all().order_by('-date')
    return render(request,'staff/activityS.html',{'activity' : activity})

def examS(request):
    exams = Exam.objects.all()
    return render(request,'staff/examS.html',{'exams':exams})

def englishS(request):
    exams = Exam.objects.all()
    return render(request,'staff/englishS.html',{'exams':exams})

def mathS(request):
    exams = Exam.objects.all()
    return render(request,'staff/mathS.html',{'exams':exams})

def othersS(request):
    exams =Exam.objects.all()
    return render(request,'staff/othersS.html',{'exams':exams})

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

def delete_news(request,**kwargs):
    pk = kwargs['pk']
    delete_news = News.objects.get(pk=pk).delete()
    return redirect('homeS')

# def get_title(request):
#     if request.method == 'POST':
#         form = AddNewsForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')

#     else:
#         form = AddNewsForm()
#     return render(request,'staff/addNews.html',{'form' : form})

def updateNews(request,**kwargs):
    pk = kwargs['pk']
    news = News.objects.get(pk=pk)
    return render(request,'staff/update_news.html',{'news':news})

def addActivity(request):
    # pylint: disable=no-member
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

def update_activity(request,**kwargs):
    pk = kwargs['pk']
    activity = Board.objects.filter(pk=pk)
    return render(request,'staff/update_activity.html',{'activity':activity})

def delete_board(request,id):
    # pylint: disable=no-member
    deleteboard = Board.objects.get(pk=id).delete()
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

def delete_english(request,id):
    #     #delete
    deleteeng = Exam.objects.get(pk=id).delete()
    
    return render(request,'staff/englishS.html')

def delete_math(request,id):
    deletemath = Exam.objects.get(pk=id).delete()
    return render(request,'staff/mathS.html')

def delete_others(request,id):
    deleteothers = Exam.objects.get(pk=id).delete()
    return render(request,'staff/otherS.html')