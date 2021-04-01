from django.db import models


from driver.models import Bus

# Create your models here.
class Parent(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=64)
    contact = models.IntegerField()
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=64)
    home_gps = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Parent"

class Kid(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(unique=True, max_length=60)
    section = models.TextField(max_length=60)
    photo = models.FileField()
    parent_id = models.ForeignKey(Parent,to_field='id',on_delete=models.CASCADE, null=False)
    bus_id = models.ForeignKey(Bus,to_field='id',on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Kid"