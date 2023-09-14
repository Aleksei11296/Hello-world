from django.db import models
from django.core.validators import MinValueValidator

class Post(models.Model):
    heading = models.CharField(
        max_length=25,
        unique=True,  # названия товаров не должны повторяться
    )
    text = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='post',  # все продукты в категории будут доступны через поле products
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return f'{self.heading.title()}: {self.text[:20]}'


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    heading = models.CharField(max_length=50, unique=True, default='Sport')

    def __str__(self):
        return self.heading.title()

# Create your models here.
