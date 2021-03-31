from django.db import models

# Create your models here.
class Bus(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Bus"

class Driver(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=64)
    contact = models.IntegerField()
    password = models.CharField(max_length=128)
    bus_id = models.ForeignKey(Bus,to_field='id',on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Driver"