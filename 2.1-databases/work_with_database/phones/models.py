from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = AutoSlugField(populate_from='name')
