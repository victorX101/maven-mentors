from django.db import models

class MenteeData(models.Model):
    CHOICES = (
        ('1349', 'Programming for Class 8th & Above'),
        ('1799', 'JOSAA + Basic Programming & Finance' ),
        ('750', 'Basic Plan for JOSAA' ),
    )
    your_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    parents_contact_number = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    referred_by = models.CharField(max_length=100)
    promocode = models.CharField(max_length=1000)
    mentor_code = models.CharField(max_length=1000)
    # When we call the object it returns name rather than a string with this str method.
    def __str__(self):
        return self.your_name
           
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
