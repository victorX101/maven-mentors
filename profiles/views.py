from django.shortcuts import render,redirect
from profiles import forms
from django.conf import settings


# Create your views here.

def home(request):
    return render(request,'profiles/base.html')

def menteereg(request):
    if(request.method == 'POST'):
        form = forms.MenteeForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request,'profiles/message.html')
        else:
            return render(request,'profiles/mentee/registration.html',context={'form':form})
    else:
        form = forms.MenteeForm()
        return render(request,'profiles/mentee/registration.html',context={'form':form})

def mentorreg(request):
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSe6q6c0XdbzCCJEgURz5Dh80faucJn6_3LAGSMULNappwkYhQ/viewform?usp=sf_link')

def terms(request):
    return render(request,'profiles/terms.html')

def carreg(request):
    return redirect('https://forms.gle/iHz63nJvF7yCtMgk6')  

def codingreg(request):
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSdvijIapiHturNRM4cM4gumc860q0ZMus40APEo8ypGzOXV5Q/viewform?usp=sf_link')


def payments(request):
    return render(request,'profiles/payments.html')