from django.db import models

# Create your models here.
class searchs(models.Model):
    search_title = models.TextField(default='type what to search')
    title        = models.TextField(default='')
    link         = models.TextField(default='')
    count        = models.DecimalField(max_digits=100,decimal_places=0,default=1)
