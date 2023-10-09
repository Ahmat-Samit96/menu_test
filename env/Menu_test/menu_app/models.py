from django.db import models 

from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.fields import AutoSlugField

# Create your models here.


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        elif self.url:
            return self.url
        else:
            return "#"
