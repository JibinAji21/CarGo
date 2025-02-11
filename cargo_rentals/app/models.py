from django.db import models

# Create your models here.

class Cars(models.Model):
    car_id=models.TextField()
    car_name=models.TextField()
    car_year=models.IntegerField()
    car_place=models.TextField()
    car_rent=models.IntegerField()
    car_fuel=models.TextField()

