from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from datetime import timedelta
from django.utils import timezone

class Address(models.Model):
    address                 = models.CharField(max_length=250)
    street                  = models.CharField(max_length=100)
    city                    = models.CharField(max_length=100)
    district                = models.CharField(max_length=100)
    state                   = models.CharField(max_length=100)
    postal_code             = models.CharField(max_length=6)


    def __str__(self) -> str:
        return self.address
class User(AbstractUser):
    email                   = models.EmailField()
    phone_regex             = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number            = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True) # Validators should be a list
    address                 = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='users', null=True)
    

    def __str__(self)->str:
        return self.phone_number
    


class Donor(models.Model):
    status_choice           = (
        ('AV','AV'),
        ('UAV','UAV')
    )

    blood_gp_choice         = (
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-')
    )


    donor                   = models.ForeignKey(User, on_delete=models.CASCADE)
    weight                  = models.FloatField()
    dob                     = models.DateField()
    status                  = models.CharField(max_length=3, choices=status_choice, default='AV')
    blood_group             = models.CharField(max_length=3, choices=blood_gp_choice)
    last_donated_date       = models.DateField(null=True, blank=True)
    points                  = models.IntegerField(default=0)
    fcm_token               = models.CharField(max_length=255, null=True, blank=True)

    def can_donate(self)->bool:
        if self.last_donated_date:
            return timezone.now().date() > self.last_donated_date + timedelta(days=90)
        return True

    def donate(self, points):
        self.last_donated_date = timezone.now().date()
        self.points += points
        self.save()
    
    def __str__(self) -> str:
        return self.donor.username

class Point(models.Model):
    point_type_choice       = (
        ('app','app'),
        ('wapp','wapp')
    )

    donor                   = models.ForeignKey(Donor, default=1, on_delete=models.CASCADE)
    point                   = models.IntegerField()
    point_type              = models.CharField(max_length=4, choices=point_type_choice, default='app')
    point_date              = models.DateTimeField()


    def __str__(self) -> str:
        return f'{self.donor.username}_{self.point_date}'
    
class Certificate(models.Model):
    name                    = models.CharField(max_length=100)
    Donor                   = models.ForeignKey(Donor, default=1,on_delete=models.CASCADE)
    is_reciever_approved    = models.BooleanField(default=False)
    issue_date              = models.DateTimeField()  

    def __str__(self) -> str:
        return self.name  
    
class BloodUnit(models.Model):
    donor                   = models.ForeignKey(Donor, on_delete=models.CASCADE)
    blood_request           = models.ForeignKey('patient.request', on_delete=models.CASCADE)
    units                   = models.IntegerField()
    date_donated            = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Blood Unit  - Donoted by {self.Donor.donor.username} and Requested by {self.blood_request.request_raised_by.user.username}'
    
