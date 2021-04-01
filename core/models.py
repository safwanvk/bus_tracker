from django.db import models

# Create your models here.
class UserType(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = "User_Type"