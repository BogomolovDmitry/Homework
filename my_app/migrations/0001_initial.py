# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 20:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id_book', models.AutoField(primary_key=True, serialize=False)),
                ('name_book', models.CharField(max_length=100, verbose_name='Название книги')),
                ('genre_book', models.CharField(default='Жанр неизвестен', max_length=50, verbose_name='Жанр')),
                ('photo', models.ImageField(blank=True, default='no-image.png', null=True, upload_to='', verbose_name='Фото')),
                ('writer_book', models.CharField(max_length=100, verbose_name='Автор')),
                ('year_book', models.IntegerField(verbose_name='Год создания')),
                ('number_book', models.IntegerField(verbose_name='Кол-во книг')),
            ],
        ),
        migrations.CreateModel(
            name='Issuance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Book')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(through='my_app.Issuance', to=settings.AUTH_USER_MODEL),
        ),
    ]
