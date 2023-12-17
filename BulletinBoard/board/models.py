from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username.title()}'

class Category(models.Model):
    tank = 'TA'
    hill = 'HI'
    dd = 'DD'
    trader = 'TR'
    master = 'MS'
    kwits = 'KW'
    blacksmiths = 'BL'
    tanners = 'TA'
    potion = 'PO'
    spell = 'SP'

    POSITIONS = [
        (tank, 'Танки'),
        (hill, 'Хилы'),
        (dd, 'ДД'),
        (trader, 'Торговцы'),
        (master, 'Гилдмастеры'),
        (kwits, 'Квестгиверы'),
        (blacksmiths, 'Кузнецы'),
        (tanners, 'Кожевники'),
        (potion, 'Зельевары'),
        (spell, 'Мастера заклинаний')
    ]
    position = models.CharField(max_length=2, choices=POSITIONS)


class Ads(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    position = models.CharField(max_length=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()

