from django.db import models

# Create your models here.

class CalcHistory(models.Model):
    first_number = models.IntegerField()
    second_number = models.IntegerField()
    third_number = models.IntegerField()
    four_number = models.IntegerField()
    first_operation = models.CharField(max_length=1)
    second_operation = models.CharField(max_length=1)
    third_operation = models.CharField(max_length=1)
    result = models.IntegerField()
