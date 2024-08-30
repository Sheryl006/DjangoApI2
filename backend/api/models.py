from django.db import models


# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='uploads/images', null=False, blank=False, default="uploads/images/profile.jpg")
    name = models.CharField(max_length=150)
    manufacturer = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    

    def __str__(self):
        return self.name

class Car(models.Model) :
    image = models.ImageField(upload_to='uploads/images', null=False, blank=False, default="uploads/images/profile.jpg")
    name = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()

    def __str__(self) :
        return self.image


class YourModel(models.Model) :
    name = models.CharField(max_length= 150)


    def __str__(self) :
        return self.name


