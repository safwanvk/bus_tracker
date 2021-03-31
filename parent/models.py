from django.db import models

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