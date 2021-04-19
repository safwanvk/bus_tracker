from django.db import models

# Create your models here.
class UserType(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = "User_Type"

class User(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    is_active = models.BooleanField()
    role_id = models.ForeignKey(UserType,to_field='id',on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        db_table = "User"

class Feedback(models.Model):
   id = models.AutoField(null=False, primary_key=True)
   name = models.CharField(max_length=50)
   email = models.CharField(max_length=50)
   title = models.CharField(max_length=200)
   message = models.CharField(max_length=500)
   date = models.DateTimeField()
   user_id = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,null=False)
   
   def __str__(self):
       return self.title

   class Meta:
        db_table = "Feedback"
