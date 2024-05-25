from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    email                   = models.EmailField()
    phone_regex             = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number            = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True) # Validators should be a list
    
    

    def __str__(self)->str:
        return self.username
    
class Address(models.Model):
    address                 = models.CharField(max_length=250)
    place                   = models.CharField(max_length=100)
    home_town               = models.CharField(max_length=100)
    district                = models.CharField(max_length=100)
    state                   = models.CharField(max_length=100)
    pincode                 = models.CharField(max_length=6)

    def __str__(self) -> str:
        return self.address

class Point(models.Model):
    point_type_choice       = (
        ('app','app'),
        ('wapp','wapp')
    )

    point                   = models.IntegerField()
    point_type              = models.CharField(max_length=4, choices=point_type_choice)
    point_date              = models.DateTimeField()

    def __str__(self) -> str:
        return self.point

class Certificate(models.Model):
    name                    = models.CharField(max_length=100)
    is_reciever_approved    = models.BooleanField(default=False)
    issue_date              = models.DateTimeField()  

    def __str__(self) -> str:
        return self.name     

class BloodUnit(models.Model):
    Donor                   = models.ForeignKey(User, on_delete=models.CASCADE )

    def __str__(self) -> str:
        return 'Blood Unit '+self.donor__user__username

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


    doner                   = models.ForeignKey(User, on_delete=models.CASCADE)
    points                  = models.ForeignKey(Point, on_delete=models.CASCADE)
    certificate             = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    wieght                  = models.FloatField()
    dop                     = models.DateField()
    status                  = models.CharField(max_length=3, choices=status_choice, default='AV')
    blood_group             = models.CharField(max_length=3, choices=blood_gp_choice)
    
    def __str__(self) -> str:
        return self.doner__user__username

