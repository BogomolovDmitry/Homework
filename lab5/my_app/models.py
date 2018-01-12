from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
        id_book = models.AutoField(primary_key=True)
        name_book = models.CharField(max_length=100)
        genre_book = models.CharField(max_length=50, default='Жанр неизвестен')
        photo = models.ImageField(null=True, blank=True)
        writer_book = models.CharField(max_length=100)
        year_book = models.DateField()
        number_book = models.IntegerField()


class Issuance(models.Model):
        id_book = models.ForeignKey(Book, on_delete=models.CASCADE)
        id_user = models.ForeignKey(User, on_delete=models.CASCADE)
