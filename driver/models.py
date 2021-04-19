from django.db import models

from core.models import *

# Create your models here.
class Bus(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    bus_no = models.TextField(max_length=60)
    description = models.TextField(max_length=600)
    objects = models.Manager()

    def __str__(self):
        return self.bus_no

    class Meta:
        db_table = "Bus"

class Driver(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    user_id = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=64)
    contact = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    bus_id = models.ForeignKey(Bus,to_field='id',on_delete=models.CASCADE, null=False)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Driver"