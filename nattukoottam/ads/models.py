from django.db import models


class Ads(models.Model):
    name                = models.CharField(max_length=50)
    pic                 = models.ImageField(upload_to='Ads', default='ads.jpeg')

    def __str__(self) -> str:
        return self.name