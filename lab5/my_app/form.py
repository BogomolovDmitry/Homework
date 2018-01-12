from .models import *
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = [""]

