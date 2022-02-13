from django.urls import path
from . import views

app_name='webtestapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('settei/', views.settei, name='settei'),
    path('otoi/', views.otoi, name='otoi'),
    path('topic/', views.topic, name='topic'),
    path('closet/', views.closet, name='closet'),
    path('riyou/', views.riyou, name='riyou'),
    path('calendar/', views.calendar, name='calendar'),
    path('timeline/', views.timeline, name='timeline'),
    path('timelinew/', views.timelinew, name='timelinew'),
    path('toukou/', views.toukou, name='toukou'),
    path('code/', views.code, name='code'),
    path('tuika/', views.tuika, name='tuika'),
    path('okiniiri/', views.okiniiri, name='okiniiri'),
    path('sakujo/', views.sakujo, name='sakujo'),
    path('honnninntoruroku/', views.honnninntoruroku, name='honnninntoruroku'),
    path('passward/', views.passward, name='passward'),
    path('clothes_register/', views.clothes_register, name='clothes_register'),
    path('help/', views.help, name='help'),
    path('forget/', views.forget, name='forget'),
    path('colour/', views.colour, name='colour')
]
