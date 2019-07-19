from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponseForbidden
from .models import User,Exam,News,Board
from django.template import loader
from django.views import generic
from django.urls import reverse
from .forms import AddNewsForm,AddExamForm,AddBoard
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def home(request,**kwargs):
    context = dict()
    news = News.objects.all().order_by('-date')
    p = Paginator(news, 5)
    if 'p' in kwargs:
        context = {'news' : p.page(kwargs['p'])}
    else:
        context = {'news' : p.page(1)}
    context += {'page': p.count}
    return render(request,'home.html',context)

def activity(request):
    board = Board.objects.all().order_by('-date')
    return render(request,'activity.html',{'board' : board})


def exam(request):
    context = dict()
    exams = Exam.objects.all()[:10]
    context['all'] = exams
    return render(request,'exam.html',context)

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
    englishs = Exam.objects.all().order_by('-date')[:10]
    return render(request,'english.html',{'englishs':englishs})

def math(request):
    maths = Exam.objects.all().order_by('-date')
    return render(request,'math.html',{'maths' : maths})

def others(request):
    otherss = Exam.objects.all().order_by('-date')
    return render(request,'others.html',{'otherss' : otherss})

@login_required
def homeS(request):
    if request.user.is_staff:
        news = News.objects.all().order_by('-date')
        return render(request,'staff/homeS.html',{'news':news})
    else:
        return HttpResponseForbidden()

def activityS(request):
    activity = Board.objects.all().order_by('-date')
    return render(request,'staff/activityS.html',{'activity' : activity})

def examS(request):
    exams = Exam.objects.all()
    eng = Exam.objects.filter(category='ENG')[:5]
    math = Exam.objects.filter(category = 'MATH')[:5]
    others = Exam.objects.filter(category = 'OTHERS')[:5]
   

    return render(request,'staff/examS.html',{'exams':exams, 'eng':eng , 'math':math,'others':others})

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
            form.save()
            #save to db
            return redirect('homeS')
    else:
        form = AddNewsForm()

    return render(request,'staff/addNews.html',{'form' : form})

def addNews_summit(request):
    # title = request.POST["title"]
    # # file = request.FILES["file"]
    # date = request.POST["date"]
    # news = News(title=title)
    # news.save()
    return redirect('homeS')

def delete_news(request,**kwargs):
    pk = kwargs['pk']
    delete_news = News.objects.filter(pk=pk).delete()
    return redirect('homeS')

def updateNews(request,**kwargs):
    pk = kwargs['pk']
    news = News.objects.get(pk=pk)
    return render(request,'staff/update_news.html',{'news':news})

def updateNews2(request,**kwargs):
    pk = kwargs['pk']
    # pylint: disable=no-member
    u = News.objects.get(pk=pk)
    if not u:
        return redirect('homeS')
    if request.method == 'POST':
        form = AddNewsForm(request.POST,request.FILES,instance=u)
        if form.is_valid():
            form.save()
            return redirect('homeS')
    else:
        form = AddNewsForm(instance=u)
    return render(request,'staff/update_news.html',{'form' : form})


def addActivity(request):
    # pylint: disable=no-member
    # activity = Board.objects.all()
    if request.method == 'POST':
        form = AddBoard(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #save to db
            return redirect('activityS')
    else:
        form = AddBoard()
    return render(request,'staff/addActivity.html',{'form':form})

def addActivity_summit(request):
    # titleboard = request.POST["titleboard"]
    # # date = request.POST['date']
    # detail = request.POST["detail"]
    # # image = request.POST["image"]
    # board = Board(titleboard=titleboard,detail=detail)
    # board.save()
    return render(request,'staff/addActivity.html')    

def update_activity(request,**kwargs):
    # pylint: disable=no-member
    pk = kwargs['pk']
    u = Board.objects.get(pk=pk)
    if not u:
        return redirect('activityS')
    if request.method == 'POST':
        form = AddBoard(request.POST,request.FILES,instance=u)
        if form.is_valid():
            form.save()
            return redirect('activityS')
    else:
        form = AddBoard(instance=u)
    return render(request,'staff/update_activity.html',{'form':form})

def delete_board(request,**kwargs):
    pk = kwargs['pk']
    # pylint: disable=no-member
    deleteboard = Board.objects.get(pk=pk).delete()
    return redirect('activityS')

def addExam(request):
    if request.method == 'POST':
        form = AddExamForm(request.POST,request.FILES,request.CHOICE)
        if form.is_valid():
            form.save()
            #save to db
            return redirect('examS')
    else:
        form = AddExamForm()
    return render(request,'staff/addExam.html',{'form':form})

def addExam_summit(request):
    # titleexam = request.POST["titleexam"]
    # link = request.POST["link"]
    # date = request.POST["date"]
    # # category = request.POST["category"]
    # exam = Exam(titleexam=titleexam,link=link,date=date)
    # exam.save()
    return redirect('examS')

def delete_english(request,id):
    #     #delete
    deleteeng = Exam.objects.get(pk=id).delete()
    
    return redirect('englishS')

def delete_math(request,id):
    deletemath = Exam.objects.get(pk=id).delete()
    return redirect('mathS')

def delete_others(request,id):
    deleteothers = Exam.objects.get(pk=id).delete()
    return redirect('othersS')

def pdf_view(request,**kwargs):
    pk=kwargs['pk']
    pdf = News.objects.get(pk=pk)
    with open('/path/to/my/file.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed