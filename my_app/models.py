from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.name}  {self.last_name} - {self.age} years old"