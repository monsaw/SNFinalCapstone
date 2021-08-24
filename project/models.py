from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 40)

    def get_absolute_url(self):
        return reverse('project:home')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length = 40)
    body = RichTextField()
    date_created = models.DateTimeField(default = timezone.now)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, related_name = 'categorys')

    def get_absolute_url(self):
        return reverse('project:home')

    def __str__(self):
        return self.title



class Registration(models.Model):
    choice = (('M','Male'),('F','Female'))
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length = 40, choices = choice , default = 'Male')

    def __str__(self):
        return self.user.username
