from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='user_image/', default='default/user_image/user.png')
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    balance = models.IntegerField(default=0)
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = ((MALE, 'male'), (FEMALE, 'female'))
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def spend(self, amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        self.save()
        return True

    def __str__(self):
        if self.username:
            return self.username
        else:
            return self.email
