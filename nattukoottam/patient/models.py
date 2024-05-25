from django.db import models

class Reciever(models.Model):
    user                    = models.ForeignKey('donor.User', on_delete=models.CASCADE)
    address                 = models.ForeignKey('donor.Address', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user__username
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

    request_raised_by       = models.ForeignKey(Reciever, on_delete= models.CASCADE, related_name='requestor')
    patient_name            = models.CharField(max_length=50)
    blood_group             = models.CharField(max_length=3, choices=blood_gp_choice)
    Hospital                = models.CharField(max_length=100)
    date                    = models.DateTimeField()
    donors                  = models.ForeignKey("donor.donor", on_delete=models.CASCADE)
    is_closed               = models.BooleanField(default=False)
    patient_address         = models.ForeignKey('donor.address', on_delete=models.CASCADE)
    blood_unit              = models.ForeignKey('donor.blood_unit', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.request_raised_by__user__username

