from django.db import models
# Create your models here.

class Beauty(models.Model):
    name=models.CharField(max_length=50)
    text=models.TextField()
    img=models.ImageField(upload_to='beauty')

    def str(self):
        return self.name

class  Products(models.Model):
    name=models.CharField(max_length=50)
    text=models.TextField()
    img=models.ImageField(upload_to='kirish')
    price=models.DecimalField(max_digits=20, decimal_places=2)
    bosh = models.CharField(max_length=50, blank=True, null=True)

    def str(self):
        return self.name

class Coment(models.Model):
     name=models.CharField(max_length=50)
     text=models.TextField()

     def __str__(self):
         return self.name


class Kirish(models.Model):
    nomi = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField(upload_to='kirish')
    

