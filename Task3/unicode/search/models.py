from django.db import models

# Create your models here.
class search(models.Model):
    search_title = models.TextField
    title = models.TextField
    link = models.TextField
    descr = models.TextField
