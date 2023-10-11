from django.db import models

# Create your models here.


from django.contrib.auth.models  import AbstractUser
from datetime import date
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):

   
    GENDER_CHOICE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]

    username = None
    email = models.EmailField(_('email_address'), unique=True)
    gender = models.CharField(max_length=20, choices= GENDER_CHOICE)
    contact_no = models.CharField(max_length=15)
    address = models.TextField(max_length=200)
    date_of_birth = models.DateField()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # REQUIRED_FIELDS = [ 'first_name', 'last_name', 'contact_no', 'address', 'date_of_birth', 'gender']


class Designation(models.Model):
    designation=models.CharField(max_length=50)


class Technology(models.Model):
    technologies=models.CharField(max_length=50)


class Employee(CustomUser):
    is_manager = models.BooleanField(default=False)
    technology = models.ForeignKey(Technology, null=True, on_delete=models.CASCADE)
    designation = models.ManyToManyField(Designation)
    year_of_experience = models.IntegerField(default=0)
    joining_date = models.DateField()


class Id_proof(models.Model):

    ID_PROOF_CHOICE = [('ADHAR CARD', 'Adhar Card'),('PAN CARD', 'Pan Card'),('DRIVING LICENSE', 'Driving License')]
    id_proof = models.CharField(max_length=50, choices=ID_PROOF_CHOICE)
    file = models.FileField()






    











# def technology_id(self):
#         return self.technologies
    
    






    



    




