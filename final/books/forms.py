from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm

class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ['last_updated', 'created_by']
