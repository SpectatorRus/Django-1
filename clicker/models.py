from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ClickerData(models.Model):
    """
    Используется в **/clicker** для сохранения результатов пользователя. \n
    hp, iq, happiness - числа \n
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hp = models.IntegerField()
    iq = models.IntegerField()
    happiness = models.IntegerField()


