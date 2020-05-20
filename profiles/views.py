from django.shortcuts import render
from profiles import forms


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
        form = forms.MenteeForm()
        return render(request,'profiles/mentee/registration.html',context={'form':form}); 