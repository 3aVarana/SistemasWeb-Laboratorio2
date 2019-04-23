from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    birthday = models.DateTimeField(auto_now_add=True)
    cellphone = models.IntegerField()

def __str__(self):
        return self.name2