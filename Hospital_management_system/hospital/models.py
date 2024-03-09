from django.db import models

# Create your models here.
class Doctors(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField(max_length=10)
    special=models.CharField(max_length=50)
     
    def __str__(self):
        return self.name
    
class Pateint(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    mobile=models.IntegerField(null=True)
    address=models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    pateint=models.ForeignKey(Pateint,on_delete=models.CASCADE)
    time=models.TimeField()
    date=models.DateField()

    def __str__(self):
        return f"{self.pateint} booked for Doc-{self.doctor}"
