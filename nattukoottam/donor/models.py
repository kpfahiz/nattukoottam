from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    email               = models.EmailField(unique= True)
    img_user            = models.ImageField(upload_to='profile_pic', default='3052.png_860.png')
    
    

    def __str__(self):
        return self.username

class Address(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address')
    address_1           = models.CharField(max_length=100)
    address_2           = models.CharField(max_length=100)
    town                = models.CharField(max_length=100)
    district            = models.CharField(max_length=100)
    state               = models.CharField(max_length=100)
    pincode             = models.CharField(max_length=50)

    def __str__(self):
        return self.user__username

class Certificate(models.Model):
    name                = models.CharField(max_length=30)
    donor               = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificate_donor')
    requestor           = models.ForeignKey('patient.reciever', on_delete=models.CASCADE, related_name='certificate_requestor')
    date_issue          = models.DateTimeField()
    is_reciever_approved= models.BooleanField(default= False)
    is_admin_approved   = models.BooleanField(default= False)
    img_certificate     = models.ImageField()

    def __str__(self) -> str:
        return self.name

class Blood_unit(models.Model):
    requestor           = models.ForeignKey('patient.Reciever', on_delete=models.CASCADE, related_name='blood_unit_requestor')
    donor               = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blood_unit_donor')
    date_creation       = models.DateTimeField()
    is_recieved         = models.BooleanField(default= False)
    is_approved         = models.BooleanField(default= False)

    def __str__(self) -> str:
        return self.requestor__user__username

class Point(models.Model):
    type_choice         = (
        ('WAPP','With App'),
        ('WOAPP','Without App')
    )

    donor               = models.ForeignKey(User, on_delete=models.CASCADE, related_name='point_donor')
    point               = models.IntegerField()
    date_point          = models.DateTimeField()
    type_of_point       = models.CharField(max_length=5,choices=type_choice)

    def __str__(self) -> str:
        return self.donor__user__username + '\'s Point'

class Donor(models.Model):

    status_choice   = (
        ('A','Available'),
        ('UA','Unavailable')
    )
    blood_gp_choice = (
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-')
    )
    user                = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donor_user')
    points              = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='points')
    certificate         = models.ForeignKey(Certificate, on_delete=models.CASCADE, related_name='donor_certificate')
    place               = models.CharField(max_length=100)
    status              = models.CharField(max_length=3, choices=status_choice)
    blood_group         = models.CharField(max_length=3, choices=blood_gp_choice)
    phone_number        = models.CharField(max_length=10)
    weight              = models.CharField(max_length=3)
    dob                 = models.DateField()
    date_last_donation  = models.DateTimeField()

    def __str__(self) -> str:
        return self.user__username
