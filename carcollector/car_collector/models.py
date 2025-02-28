from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
class Tag(models.Model): 
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Modification(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="modifications")
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} on {self.car}"
