from django.db import models

# Create your models here.
class Bus(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Bus"