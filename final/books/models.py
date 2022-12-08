from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    year = models.PositiveIntegerField(null=True)
    rating = models.FloatField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    description = models.TextField(null=True, blank=True)
    created_by = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
