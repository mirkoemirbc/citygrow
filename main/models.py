from __future__ import unicode_literals

from django.db import models

# Create your models here.


class WDMCityMapItemType(models.Model):
    name = models.CharField(max_length=64)
    image_name = models.CharField(max_length=64)


class WDMWorldMapItemType(models.Model):
    name = models.CharField(max_length=64)
    image_name = models.CharField(max_length=64)


class WDMCityType(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


class WDMCity(models.Model):
    name = models.CharField(max_length=64)
    city_type_id = models.ForeignKey('main.WDMCityType',
                                     on_delete=models.PROTECT)


class WDMCityMap(models.Model):
    city_x = models.IntegerField(default=0)
    city_y = models.IntegerField(default=0)
    city_id = models.ForeignKey('main.WDMCity', on_delete=models.PROTECT)
    cmit_id = models.ForeignKey('main.WDMCityMapItemType',
                                on_delete=models.PROTECT)
