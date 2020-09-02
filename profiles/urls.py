from django.urls import path
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('',views.home,name='home'),
    path('mentee/registration/',views.menteereg,name='menteereg'),
    path('terms/',views.terms,name='terms'),
    path('mentor/registration/',views.mentorreg,name='mentorreg'),
    path('ca/registration/',views.carreg,name='careg'),
    path('payments/' , views.payments,name ='payments'),
    path('check/',views.check,name = 'check'),
]

