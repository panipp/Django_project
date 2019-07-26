from django.urls import path
from scinews.views import (home,activity,exam,news,subject
,addNews_summit,activity2,homeS,activityS,examS,addNews,updateNews,updateNews2,delete_news,addActivity,addActivity,
addActivity_summit,update_activity,delete_board,addExam,addExam_summit,pdf_view,)

app_name = 'scinews'

urlpatterns = [
    path('',home,name='home'),
    path('home/<int:p>/',home,name='home'),

    path('activity/',activity,name='activity'),
    path('activity2/<int:pk>/',activity2,name='activity2'),
    path('activity/id/<int:id>/',activity,name='activity'),

    path('exam/',exam,name='exam'),
    path('exam/<str:name>/',subject,name='examsub'),

    path('news/<int:pk>/',news,name='news'),

    path('addNews_summit/',addNews_summit,name='addNews_summit'),
    # path('activity2/<int:pk>/',activity2,name='activity2'),
    # path('english/',english,name='english'),
    # path('math/',math,name='math'),
    # path('others/',others,name='others'),

    path('homeS/',homeS,name='homeS'),
    path('activityS/',activityS,name='activityS'),
    path('examS/',examS,name='examS'),
    # path('englishS/',englishS,name='englishS'),
    # path('delete_english/<int:id>',delete_english,name="delete_english"),
    # path('mathS/',mathS,name='mathS'),
    # path('delete_math/<int:id>',delete_math,name="delete_math"),
    # path('othersS/',othersS,name='othersS'),
    # path('delete_others/<int:id>',delete_others,name='delete_others'),
    path('addNews/',addNews,name='addNews'),
    path('updateNews/<int:pk>/',updateNews,name='updateNews'),
    path('updateNews2/<int:pk>/',updateNews2,name='updateNews2'),
    path('delete_news/<int:pk>/',delete_news,name='delete_news'),
    path('addActivity/',addActivity,name='addActivity'),
    path('addActivity_summit/',addActivity_summit,name='addActivity_summit'),
    path('update_activity/<int:pk>/',update_activity,name='update_activity'),
    path('delete_board/<int:pk>',delete_board,name="delete_board"),
    path('addExam/',addExam,name='addExam'),
    path('addExam_summit/',addExam_summit,name="addExam_summit"),
    path('pdf_view/<int:id>/',pdf_view,name="pdf_view"),
]