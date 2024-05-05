from django.db import models


class News(models.Model):
    heading             = models.CharField(max_length=500)
    title               = models.TextField()
    date                = models.DateTimeField()
    pic                 = models.ImageField(upload_to='News', default='ads.jpeg')
    content             = models.TextField()

    def __str__(self) -> str:
        return self.heading