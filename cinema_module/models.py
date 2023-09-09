from django.db import models


# Create your models here.
class Cinema(models.Model):
    image = models.ImageField(upload_to='cinema_image', null=True, blank=True)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name
