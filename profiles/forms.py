from django import forms
from profiles import models
from django.core.validators import RegexValidator
import re

phone_re = re.compile(r'^[\d]{10}$')
phone_validator = RegexValidator(regex=phone_re, message='Invalid phone number')

class MenteeForm(forms.ModelForm):
    CHOICES = (
        ('1349', 'Programming for Class 8th & Above'),
        ('1799', 'JOSAA + Programming' ),
        ('750', 'Basic Plan for JOSAA' ),
    )
    choice = (
        ('Yes', 'Yes, I have a laptop/PC for classes'),
        ('No', 'No, I dont have a Laptop/PC' ),
        ('will arrange','I will arrange a Laptop/PC for classes' ),
    )
    students_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Elon Musk'}),label= "Student\'s name")
    students_number = forms.CharField(max_length=10, widget=forms.NumberInput(attrs={'class':'input100','placeholder':'10 digit number(without +91)'}),validators=[phone_validator],label= "Student\'s number")
    parents_number = forms.CharField(max_length=10,label = 'Parents Number:',widget=forms.NumberInput(attrs={'class':'input100','placeholder':'10 digit number(without +91)'}),validators=[phone_validator])   
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'City'}))
    school = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Type NA if you are 12th passout'}),required=True)
    referred_by = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'How do you get to know about us ?'}),required=True)
    promocode = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Promocode if any ?'}),required=False)
    mentor_code = forms.ChoiceField(widget=forms.Select(attrs={'class':'input100','placeholder':'Year'}),choices=CHOICES, label="Select a Plan",required=True )
    laptop = forms.ChoiceField(widget=forms.Select(attrs={'class':'input100','placeholder':'Year'}),choices=choice, required = True , label="Please Select one")
    class Meta:
        model = models.MenteeData
        fields = [
            'students_name',
            'students_number',
            'parents_number',
            'location',
            'school',
            'referred_by',
            'promocode',
            'mentor_code',
            'laptop',
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