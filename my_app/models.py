from django.db import models
from datetime import datetime, date

class Member(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    
    
    def __str__(self):
        return f"{self.name}  {self.last_name} - {self.age} years old. Today's date: {str(self.birth_date)}"
    
    