from django.db import models

# Create your models here.


from django.contrib.auth.models  import AbstractUser
from datetime import date
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.utils.text import slugify


class CustomUser(AbstractUser):

   
    GENDER_CHOICE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]

    username = None
    #groups = None
    #user_permissions = None
    email = models.EmailField(_('email_address'), unique=True)
    gender = models.CharField(max_length=20, choices= GENDER_CHOICE)
    contact_no = models.CharField(max_length=15)
    address = models.TextField(max_length=200)
    date_of_birth = models.DateField(null=True,blank=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)


    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    # REQUIRED_FIELDS = [ 'first_name', 'last_name', 'contact_no', 'address', 'date_of_birth', 'gender']


class Designation(models.Model):
    designation=models.CharField(max_length=50)

    def __str__(self):
        return self.designation


class Technology(models.Model):
    technologies=models.CharField(max_length=50)

    def __str__(self):
        return self.technologies

class Employee(CustomUser):
    ID_PROOF_CHOICE = [
        ('ADHAR CARD', 'Adhar Card'),
        ('PAN CARD', 'Pan Card'),
        ('DRIVING LICENSE','Driving License')
        ]
    
    is_manager = models.BooleanField(default=False)
    technology = models.ManyToManyField(Technology)
    designation = models.ForeignKey(Designation, null=True, on_delete=models.SET_NULL)
    year_of_experience = models.IntegerField(default=0)
    joining_date = models.DateField()
    id_proof = models.CharField(max_length=50, choices=ID_PROOF_CHOICE, null=True)
    id_proof_file = models.FileField(upload_to='documents/', null=True)








    











# def technology_id(self):
#         return self.technologies
    
    






    



    




