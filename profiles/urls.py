from django.urls import path
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('',views.home,name='home'),
    path('mentee/registration/',views.menteereg,name='menteereg'),
   # path('mentor/guidelines/'veiws.home,name="mentorguide"),
    path('mentor/registration/',views.home,name='mentorreg'),
    path('ca/registration/',views.home,name='careg'),
    
]

