# models.py
from django.db import models
class Osoba(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    age = models.IntegerField()
    adress=models.CharField(max_length=60)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.name




class Samochod(models.Model):
    model = models.CharField(max_length=60)
    marka = models.CharField(max_length=60)
    rokprodukcji = models.IntegerField()
    wypozyczajacy = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    def __str__(self):
        return self.model