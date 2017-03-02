import datetime
from django.db import models
from django.utils import timezone
# Create your models here. not sure if this is right
#will use this to filter entries

#entry has entry and publication date
class Entry(models.Model):
    date = models.DateTimeField(default = timezone.now())
    author = models.CharField(max_length=200,default='stephen king')
    title = models.CharField(max_length=200,default='twilight')
    text = models.TextField(max_length=1000,default='stephen king')


    def __str__(self):
        return self.title

