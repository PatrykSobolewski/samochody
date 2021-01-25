# models.py
from django.db import models
class Osoba(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    def __str__(self):
        return self.name