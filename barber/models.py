from distutils.text_file import TextFile
from mimetypes import init
from django.db import models
from django.forms import CharField, Textarea

# Create your models here.
class FAQ(models.Model):
    question = CharField(max_length=100)
    answer = CharField()
    