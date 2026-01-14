from django.db import models
from django.contrib.auth.models import User

from blog.models import Products


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ism = models.CharField(max_length=50, null=True, blank=True)
    familiya = models.CharField(max_length=50, null=True, blank=True)
    tug_sana = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='profile/',null=True, blank=True)
    nomer = models.CharField(max_length=13,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Izoh(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username



