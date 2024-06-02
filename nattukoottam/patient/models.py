from django.db import models

class Receiver(models.Model):
    user                    = models.ForeignKey('donor.User', on_delete=models.CASCADE)
    is_receiver             = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username
    
class Request(models.Model):
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

    request_raised_by       = models.ForeignKey(Receiver, on_delete= models.CASCADE, related_name='requestor')
    patient_name            = models.CharField(max_length=50)
    blood_group             = models.CharField(max_length=3, choices=blood_gp_choice)
    Hospital                = models.CharField(max_length=100)
    date                    = models.DateTimeField()
    is_closed               = models.BooleanField(default=False)
    patient_address         = models.ForeignKey('donor.address', on_delete=models.CASCADE)
    blood_unit              = models.ForeignKey('donor.bloodunit', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.request_raised_by.user.username
    

class Donation(models.Model):
    donor = models.ForeignKey('donor.donor', on_delete=models.CASCADE)
    blood_request = models.ForeignKey(Request, on_delete=models.CASCADE)
    date_donated = models.DateTimeField(auto_now_add=True)
    approved_by_receiver = models.BooleanField(default=False)

    def approve_donation(self):
        if not self.approved_by_receiver:
            self.approved_by_receiver = True
            self.save()
            #self.donor.donate(points=10)
            self.generate_certificate()

    def generate_certificate(self):
        # Code to generate a certificate
        pass
    
    def __str__(self) -> str:
        return f'Doantion {self.blood_request.request_raised_by.user.username}'