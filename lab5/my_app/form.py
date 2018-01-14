from .models import *
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["id_book", "name_book", "genre_book", "photo", "writer_book", "year_book"]

