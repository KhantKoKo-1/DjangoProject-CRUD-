from django.db import models

# Create your models here.

class Users(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=16)

    def __str__(self):
        return self.user_name
class Writer(models.Model):

    firstName =  models.CharField(max_length=100)
    lastName  = models.CharField(max_length=100)      

    def __str__(self):
        return self.firstName + ' ' +self.lastName
    
class Book(models.Model):
    
    name = models.CharField(max_length=100,null=False)
    writer =models.ForeignKey(Writer, on_delete = models.SET_NULL,null=True)
    
    def __str__(self):
        return self.name
   