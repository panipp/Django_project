from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseNotFound
from .models import User,CategoryExam,Exam,News,Board
from django.template import loader
from django.views import generic
from django.urls import reverse
from .forms import AddNewsForm,AddExamForm,AddBoard
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from scinews.helper import check_permission

# ------------------Student-------------------
def home(request,**kwargs):
    news = News.objects.all().order_by('-date')
    p = Paginator(news, 5)
    page = request.GET.get('page')
    news = p.get_page(page)
    return render(request,'home.html',{'news': news})

@login_required
def activity(request,**kwargs):
    board = Board.objects.all().order_by('-date')
    p = Paginator(board, 5)
    page = request.GET.get('page')
    board = p.get_page(page)
    return render(request,'activity.html',{'board': board})

@login_required
def exam(request):
    context = dict()
    cate = dict()

    catExams = CategoryExam.objects.all()
    for cat in catExams:
        cate[str(cat)] = Exam.objects.filter(category=cat)[:5]
    context['category'] = cate
    return render(request,'exam.html',context)

@login_required
def news(request,**kwargs):
     # pylint: disable=no-member
    pk = kwargs['pk']
    news = News.objects.get(pk=pk)
    return render(request,'news.html',{'news': news })

@login_required
def activity2(request,**kwargs):
    pk = kwargs['pk']
    activity2 = Board.objects.get(pk=pk)
    return render(request,'activity2.html',{'activity2' : activity2})

@login_required
def subject(request, **kwargs):
    context = dict()
    catExams = Exam.objects.filter(category__name=kwargs['name'])
    context['namesub'] = catExams[0].category.name
    context['allsub'] = catExams
    return render(request,'subj.html',context)

def pdf_view(request,**kwargs):
    pk=kwargs['pk']
    pdf = News.objects.get(pk=pk)
    with open('/path/to/my/file.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed
    
# ------------------Student-------------------

# def english(request,):
#     englishs = Exam.objects.all().order_by('-date')[:10]
#     return render(request,'english.html',{'englishs':englishs})

# def math(request):
#     maths = Exam.objects.all().order_by('-date')
#     return render(request,'math.html',{'maths' : maths})

# def others(request):
#     otherss = Exam.objects.all().order_by('-date')
#     return render(request,'others.html',{'otherss' : otherss})

# ------------------Staff-------------------
@login_required
def homeS(request):
    if check_permission(request):
        news = News.objects.all().order_by('-date')
        p = Paginator(news, 5)
        page = request.GET.get('page')
        news = p.get_page(page)
        return render(request,'home.html',{'news':news})
    else:
        return HttpResponseForbidden()

@login_required
def activityS(request):
    if check_permission(request):
        activity = Board.objects.all().order_by('-date')
        p = Paginator(activity, 5)
        page = request.GET.get('page')
        activity = p.get_page(page)
        return render(request,'activity.html',{'activity' : activity})

@login_required
def examS(request):
    if check_permission(request):
        context = dict()
        cate = dict()
        exams = Exam.objects.all()
        context['all'] = exams

        catExams = CategoryExam.objects.all()
        for cat in catExams:
            cate[str(cat)] = Exam.objects.filter(category=cat)[:5]
        context['category'] = cate
        return render(request,'exam.html',context)

# def englishS(request):
#     exams = Exam.objects.all()
#     return render(request,'staff/englishS.html',{'exams':exams})

# def mathS(request):
#     exams = Exam.objects.all()
#     return render(request,'staff/mathS.html',{'exams':exams})

# def othersS(request):
#     exams =Exam.objects.all()
#     return render(request,'staff/othersS.html',{'exams':exams})

@login_required
def addNews(request):
    if check_permission(request):
        if request.method == 'POST':
            form = AddNewsForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                #save to db
                return redirect('home.html')
        else:
            form = AddNewsForm()

        return render(request,'staff/addNews.html',{'form' : form})

@login_required
def addNews_summit(request):
    if check_permission(request):
        # title = request.POST["title"]
        # # file = request.FILES["file"]
        # date = request.POST["date"]
        # news = News(title=title)
        # news.save()
        return redirect('home.html')

@login_required
def delete_news(request,**kwargs):
    if check_permission(request):
        pk = kwargs['pk']
        News.objects.filter(pk=pk).delete()
        return redirect('/')

@login_required
def updateNews(request,**kwargs):
    if check_permission(request):
        pk = kwargs['pk']
        news = News.objects.get(pk=pk)
        return render(request,'staff/update_news.html',{'news':news})

@login_required
def updateNews2(request,**kwargs):
    if check_permission(request):
        pk = kwargs['pk']
        # pylint: disable=no-member
        u = News.objects.get(pk=pk)
        if not u:
            return redirect('home.html')
        if request.method == 'POST':
            form = AddNewsForm(request.POST,request.FILES,instance=u)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = AddNewsForm(instance=u)
        return render(request,'staff/update_news.html',{'form' : form})

@login_required
def addActivity(request):
    if check_permission(request):
        # pylint: disable=no-member
        # activity = Board.objects.all()
        if request.method == 'POST':
            form = AddBoard(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                #save to db
                return redirect('/activity')
        else:
            form = AddBoard()
        return render(request,'staff/addActivity.html',{'form':form})

@login_required
def addActivity_summit(request):
    if check_permission(request):
        # titleboard = request.POST["titleboard"]
        # # date = request.POST['date']
        # detail = request.POST["detail"]
        # # image = request.POST["image"]
        # board = Board(titleboard=titleboard,detail=detail)
        # board.save()
        return render(request,'staff/addActivity.html')    

@login_required
def update_activity(request,**kwargs):
    if check_permission(request):
        # pylint: disable=no-member
        pk = kwargs['pk']
        u = Board.objects.get(pk=pk)
        if not u:
            return redirect('/activity')
        if request.method == 'POST':
            form = AddBoard(request.POST,request.FILES,instance=u)
            if form.is_valid():
                form.save()
                return redirect('/activity')
        else:
            form = AddBoard(instance=u)
        return render(request,'staff/update_activity.html',{'form':form})

@login_required
def delete_board(request,**kwargs):
    if check_permission(request):
        pk = kwargs['pk']
        # pylint: disable=no-member
        Board.objects.get(pk=pk).delete()
        return redirect('/activity')

@login_required
def addExam(request):
    if check_permission(request):
        if request.method == 'POST':
            form = AddExamForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                #save to db
                return redirect('exam.html')
        else:
            form = AddExamForm()
        return render(request,'staff/addExam.html',{'form':form})

@login_required
def addExam_summit(request):
    if check_permission(request):
        # titleexam = request.POST["titleexam"]
        # link = request.POST["link"]
        # date = request.POST["date"]
        # # category = request.POST["category"]
        # exam = Exam(titleexam=titleexam,link=link,date=date)
        # exam.save()
        return redirect('exam.html')

# def delete_english(request,id):
#     #     #delete
#     deleteeng = Exam.objects.get(pk=id).delete()
    
#     return redirect('englishS')

# def delete_math(request,id):
#     deletemath = Exam.objects.get(pk=id).delete()
#     return redirect('mathS')

# def delete_others(request,id):
#     deleteothers = Exam.objects.get(pk=id).delete()
#     return redirect('othersS')

# ------------------Staff-------------------