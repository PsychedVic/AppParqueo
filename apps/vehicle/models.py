from django.db import models

class VehicleType(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name

class Park(models.Model):
    PCHOICES = [
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
    ]
    FCHOICES = [
        ("1","1"),
        ("2","2"),
        ("3","3"),
    ]
    floor = models.CharField(max_length=4, choices=FCHOICES)
    parking_spot = models.CharField(max_length=4, choices=PCHOICES)
    def __str__(self):
        return "Floor: " + self.floor + " Spot: " + self.parking_spot

class Vehicle(models.Model):
    Vehicle_type = models.ForeignKey(VehicleType, on_delete = models.PROTECT)
    plate = models.CharField(max_length=10)
    color = models.TextField(max_length=10)
    spot = models.ManyToManyField(Park, through="Asign")

    def __str__(self):
        return self.plate

class Asign(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    spot = models.ForeignKey(Park, on_delete=models.CASCADE)
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    def __str__(self):
        return self.vehicle.plate



    
