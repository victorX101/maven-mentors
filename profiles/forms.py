from django.contrib.auth.forms import UserCreationForm
from django import forms
from profiles import models
from django.contrib.auth.models import User

class MenteeForm(forms.ModelForm):
    CHOICES = (
        ('1199', 'JOSAA + Basic Programming & Finance' ),
        ('750', 'Basic Plan for JOSAA' ),
        ('1999', 'Expert Mentor & Customized Plan')
    )
    your_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Elon Musk'}))
    contact_number = forms.CharField(max_length=10, widget=forms.NumberInput(attrs={'class':'input100','placeholder':'1234567890'})) #validators=[phone_validator])
    parents_contact_number = forms.CharField(max_length=10,label = 'Parents Number:',widget=forms.NumberInput(attrs={'class':'input100','placeholder':'1234567890'})) #validators=[phone_validator])   
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'City'}))
    referred_by = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'How do you get to know about us ?'}),required=True)
    promocode = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Promocode if any ?'}),required=False)
    mentor_code = forms.ChoiceField(widget=forms.Select(attrs={'class':'input100','placeholder':'Year'}),choices=CHOICES, label="Select a Plan",required=True )

    class Meta:
        model = models.MenteeData
        fields = [
            'your_name',
            'contact_number',
            'parents_contact_number',
            'location',
            'referred_by',
            'promocode',
            'mentor_code',
        ]


# class MentorForm(forms.ModelForm):
#     your_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Elon Musk'}))
#     contact_number = forms.CharField(max_length=10, widget=forms.NumberInput(attrs={'class':'input100','placeholder':'123467890'})) # validators=[phone_validator])
#     college = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':'input100','placeholder':''}))
#     email = forms.EmailField(max_length=1000, widget=forms.TextInput(attrs={'class':'input100','placeholder':'hello@example.com'}))
#     location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Ludhiana'}))
#     why_mentor = forms.CharField(max_length=10000, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Why do you think you will be a good mentor?'}))
#     linkedin_id = forms.URLField(max_length=1000, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Paste Linkedin Profile link else Leave empty if no profile'}),required= False)

    

    
#     class Meta:
#         model = models.MentorData
#         fields = [
#             'your_name',
#             'contact_number',
#             'college',
#             'email',
#             'location',
#             'why_mentor',
#             'linkedin_id',
#         ]


# class AmbassadorForm(forms.ModelForm):
#     your_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Elon Musk'}))
#     contact_number = forms.CharField(max_length=10, widget=forms.NumberInput(attrs={'class':'input100','placeholder':'123467890'})) #validators=[phone_validator])
#     college = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':'input100','placeholder':''}))
#     email = forms.EmailField(max_length=1000, widget=forms.TextInput(attrs={'class':'input100','placeholder':'hello@example.com'}))
#     location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Ludhiana'}))
    
#     class Meta:
#         model = models.AmbassadorData
#         fields = [
#             'your_name',
#             'contact_number',
#             'college',
#             'email',
#             'location',
#         ]