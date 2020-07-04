from django.shortcuts import render,redirect
from profiles import forms
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    return render(request,'profiles/base.html')

def menteereg(request):
    if(request.method == 'POST'):
        form = forms.MenteeForm(request.POST)
        if(form.is_valid()):
            form.save()
            send_mail('New Mentee Registration by '+form.cleaned_data['your_name'],'--',settings.EMAIL_HOST_USER,['teammavenmentors@gmail.com'],fail_silently=True)
            return render(request,'profiles/message.html')
        else:
            return render(request,'profiles/mentee/registration.html',context={'form':form})
    else:
        form = forms.MenteeForm()
        return render(request,'profiles/mentee/registration.html',context={'form':form})

def mentorreg(request):
    return redirect('https://forms.gle/zxJd9HZdtqXUrFEr5')
    # if(request.method == 'POST'):
    #     form = forms.MentorForm(request.POST)
    #     if(form.is_valid()):
    #         form.save()
    #         return render(request,'profiles/message.html')
    # else:
    #     form = forms.MentorForm()
    #     return render(request,'profiles/mentor/registration.html',context={'form':form})

def terms(request):
    return render(request,'profiles/terms.html')

def carreg(request):
    return redirect('https://forms.gle/iHz63nJvF7yCtMgk6')
    # if(request.method == 'POST'):
    #     form = forms.AmbassadorForm(request.POST)
    #     if(form.is_valid()):
    #         form.save()
    #         return render(request,'profiles/message.html')
    # else:
    #     form = forms.AmbassadorForm()
    #     return render(request,'profiles/ambassador/registration.html',context={'form':form})    