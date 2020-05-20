from django.db import models

class MenteeData(models.Model):
    CHOICES = (
        ('before', 'Mentor Needed Before JEE' ),
        ('after', 'Mentor Needed After JEE' ),
    )
    your_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    parents_contact_number = models.CharField(max_length=10)
    coaching_name = models.CharField(max_length=1000)
    school_name = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    referred_by = models.CharField(max_length=100)
    requirements = models.CharField(max_length=1000)
    mentor_code = models.CharField(max_length=1000)
    # When we call the object it returns name rather than a string with this str method.
    def __str__(self):
        return self.your_name


class MentorData(models.Model):
    your_name = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=10)
    college = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    location = models.CharField(max_length=100)
    why_mentor = models.CharField(max_length=10000)
    linkedin_id = models.CharField(max_length=1000)
    how_mentor = models.BooleanField()

    def __str__(self):
        return self.your_name


class AmbassadorData(models.Model):
    your_name = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=10)
    college = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.your_name
