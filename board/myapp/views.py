from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def activity(request):
    return render(request,'activity.html')

def exam(request):
    return render(request,'exam.html')