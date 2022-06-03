from django.db import models


class Phone(models.Model):
    id = models.PositiveIntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=False)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")

