from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # legat 1-1 cu User
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    postal_code = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

