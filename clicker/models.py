from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ClickerData(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hp = models.IntegerField()
    iq = models.IntegerField()
    happiness = models.IntegerField()


