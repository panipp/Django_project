from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def activity(request):
    return render(request,'activity.html')

def exam(request):
    return render(request,'exam.html')

def news(request):
    return render(request,'news.html')

def activity2(request):
    return render(request,'activity2.html')

def english(request):
    return render(request,'english.html')

def math(request):
    return render(request,'math.html')

def others(request):
    return render(request,'others.html')

def homeS(request):
    return render(request,'staff/homeS.html')

def activityS(request):
    return render(request,'staff/activityS.html')

def examS(request):
    return render(request,'staff/examS.html')

def englishS(request):
    return render(request,'staff/englishS.html')

def mathS(request):
    return render(request,'staff/mathS.html')

def othersS(request):
    return render(request,'staff/othersS.html')

def addNews(request):
    return render(request,'staff/addNews.html')

def updateNews(request):
    return render(request,'staff/update_news.html')

def addActivity(request):
    return render(request,'staff/addActivity.html')

def updateActivity(request):
    return render(request,'staff/update_activity.html')

def addExam(request):
    return render(request,'staff/addExam.html')