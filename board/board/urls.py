"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('activity/',views.activity,name='activity'),
    path('exam/',views.exam,name='exam'),
    path('news/',views.news,name='news'),
    path('activity2/',views.activity2,name='activity2'),
    path('english/',views.english,name='english'),
    path('math/',views.math,name='math'),
    path('others/',views.others,name='others'),
    path('homeS/',views.homeS,name='homeS'),
    path('activityS/',views.activityS,name='activityS'),
    path('examS/',views.examS,name='examS'),
    path('englishS/',views.englishS,name='englishS'),
    path('mathS/',views.mathS,name='mathS'),
    path('othersS/',views.othersS,name='othersS'),
    path('addNews/',views.addNews,name='addNews'),
    path('updateNews/',views.updateNews,name='updateNews'),
    path('addActivity/',views.addActivity,name='addActivity'),
    path('updateActivity/',views.updateActivity,name='updateActivity'),
    path('addExam/',views.addExam,name='addExam'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

