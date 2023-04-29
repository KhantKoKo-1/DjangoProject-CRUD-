from django.db import models

# Create your models here.

class Users(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=16)

    def __str__(self):
        return self.user_name

class Writer(models.Model):

    firstName =  models.CharField(max_length=100,unique=True)
    lastName  = models.CharField(max_length=100) 
    dob = models.DateField(null=True)     


    def __str__(self):
        return self.firstName + ' ' +self.lastName
    
class Book(models.Model):
    
    name = models.CharField(max_length=100,null=False,unique=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    writer =models.ForeignKey(Writer, on_delete = models.SET_NULL,null=True)
    book_Img = models.ImageField(upload_to='images/',null=True) 
    
    def __str__(self):
        return self.name
    

class FavBookCollection(models.Model):

        fav_name = models.CharField( max_length=50,unique=True)

        book_name = models.ManyToManyField(Book)

        def __str__(self):
           
            return self.fav_name

   