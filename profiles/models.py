from django.db import models

class MenteeData(models.Model):
    CHOICES = (
        ('1349', 'Programming for Class 8th & Above'),
        ('1799', 'JOSAA + Basic Programming & Finance' ),
        ('750', 'Basic Plan for JOSAA' ),
    )
    choice = (
        ('Yes', 'Yes, I have a laptop/PC for classes'),
        ('No', 'No, I dont have a Laptop/PC'),
        ('will arrange','I will arrange it for classes' ),
    )
    students_name = models.CharField(max_length=100)
    students_number = models.CharField(max_length=10)
    parents_number = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    school = models.CharField(max_length=200 , default="School")
    referred_by = models.CharField(max_length=100)
    promocode = models.CharField(max_length=100)
    mentor_code = models.CharField(max_length=100)
    laptop = models.CharField(max_length=100 , default="Yes,I have a laptop/PC for classes")
    # When we call the object it returns name rather than a string with this str method.
    def __str__(self):
        return self.students_name
           
# class MentorData(models.Model):
#     your_name = models.CharField(max_length=100, null=True)
#     contact_number = models.CharField(max_length=10)
#     college = models.CharField(max_length=1000)
#     email = models.EmailField(max_length=1000)
#     location = models.CharField(max_length=100)
#     why_mentor = models.CharField(max_length=10000)
#     linkedin_id = models.CharField(max_length=1000)

#     def __str__(self):
#         return self.your_name

# class AmbassadorData(models.Model):
#     your_name = models.CharField(max_length=100, null=True)
#     contact_number = models.CharField(max_length=10)
#     college = models.CharField(max_length=1000)
#     email = models.EmailField(max_length=1000)
#     location = models.CharField(max_length=100)

#     def __str__(self):
#         return self.your_name
