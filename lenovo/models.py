from django.db import models
from django.contrib.auth.models import User

class lenovothink(models.Model):
    user = models.ForeignKey(User, on_delete = True)
    name = models.CharField(max_length = 25)
    brand = models.CharField(max_length = 10)
    harddrive = models.CharField(max_length = 5)
    value = models.DecimalField(max_digits= 7, decimal_places= 2)
    material = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
