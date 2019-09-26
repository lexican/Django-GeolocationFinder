from django.db import models


class General_details(models.Model):
    ip = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    continent_code = models.CharField(max_length=100)
    continent_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    region_code = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(default="null", max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.ip