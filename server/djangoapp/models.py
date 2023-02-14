from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake (models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class CarModel (models.Model):
    SEDAN = 'SD'
    SUV ='SU'
    WAGON ='WG'
    TYPE_CHOICES = [(SEDAN,'SEDAN'),(SUV,'SUV'),(WAGON,'WAGON')]
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id=models.IntegerField()
    name = models.CharField(max_length=255)
    car_type= models.CharField(max_length=255, choices=TYPE_CHOICES,default=SEDAN)
    year = models.DateField()

    def __str__(self):
         return f"{self.make} {self.name} {self.year}"

class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip
    def __str__(self):
        return "Dealer name: " + self.full_name