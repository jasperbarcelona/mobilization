from __future__ import unicode_literals
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=60)
    island = models.CharField(max_length=20)
    number_of_cities = models.IntegerField()
    number_of_barangays = models.IntegerField()
    number_of_clusters = models.IntegerField()
    number_of_households = models.IntegerField()
    number_of_citizens = models.IntegerField()

class City(models.Model):
    name = models.CharField(max_length=60)
    region_id = models.IntegerField()
    region_name = models.CharField(max_length=60)
    number_of_barangays = models.IntegerField()
    number_of_clusters = models.IntegerField()
    number_of_households = models.IntegerField()
    number_of_citizens = models.IntegerField()

class Barangay(models.Model):
    name = models.CharField(max_length=60)
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=60)
    region_id = models.IntegerField()
    region_name = models.CharField(max_length=60)
    number_of_clusters = models.IntegerField()
    number_of_households = models.IntegerField()
    number_of_citizens = models.IntegerField()

class Cluster(models.Model):
    name = models.CharField(max_length=120)
    barangay_id = models.IntegerField()
    barangay_name = models.CharField(max_length=60)
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=60)
    region_id = models.IntegerField()
    region_name = models.CharField(max_length=60)
    number_of_households = models.IntegerField()
    number_of_citizens = models.IntegerField()
    cluster_head_id = models.IntegerField()
    cluster_head_name = models.CharField(max_length=100)

class Household(models.Model):
    name = models.CharField(max_length=60)
    cluster_id = models.IntegerField()
    cluster_name = models.CharField(max_length=120)
    barangay_id = models.IntegerField()
    barangay_name = models.CharField(max_length=60)
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=60)
    region_id = models.IntegerField()
    region_name = models.CharField(max_length=60)
    household_head_id = models.IntegerField()
    household_head_name = models.CharField(max_length=100)
    number_of_citizens = models.IntegerField()
    address = models.TextField()
    status_code = models.CharField(max_length=60)

class Citizen(models.Model):
    last_name = models.CharField(max_length=60)
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
    address = models.TextField()
    gender = models.CharField(max_length=15)
    age = models.IntegerField()
    birthday = models.DateTimeField()
    employed = models.BooleanField()
    occupation = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=30)
    religion = models.CharField(max_length=30)
    civil_status = models.CharField(max_length=30)
    spouse_name = models.CharField(max_length=120)
    spouse_age = models.CharField(max_length=120)
    msisdn = models.CharField(max_length=15)
    household_id = models.IntegerField()
    household_name = models.CharField(max_length=120)
    cluster_id = models.IntegerField()
    cluster_name = models.CharField(max_length=120)
    barangay_id = models.IntegerField()
    barangay_name = models.CharField(max_length=60)
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=60)
    region_id = models.IntegerField()
    region_name = models.CharField(max_length=60)

class ParentChild(models.Model):
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    relation = models.CharField(max_length=60)