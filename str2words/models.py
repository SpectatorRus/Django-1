from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Word(models.Model):
    """
    Используется в **/str2words** для хранения разбора стоки на слова и символы.
    """
    date = models.DateField()
    time = models.TimeField()
    inputtedString = models.CharField(max_length=100)
    words_count = models.IntegerField()
    symbols_count = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
