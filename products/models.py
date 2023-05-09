from django.db import models

# Create your models here.
# -- LAPTOP
class prod(models.Model):
    img = models.TextField()
    title = models.TextField()
    disc = models.TextField()
    price = models.IntegerField()


    
class number(models.Model):
    no = models.IntegerField() # 1 
    
#----------------------------------------

class mobile(models.Model):
    img = models.TextField()
    title = models.TextField()
    disc = models.TextField()
    price = models.IntegerField()
       
class nomob(models.Model):
    no = models.IntegerField() # 1 
    
    
#----------------------------------------

class acc(models.Model):
    img = models.TextField()
    title = models.TextField()
    disc = models.TextField()
    price = models.IntegerField()
    
    
class noacc(models.Model):
    no = models.IntegerField() # 1 
    
    
#----------------------------------------

class all(models.Model):
    img = models.TextField()
    title = models.TextField()
    disc = models.TextField()
    price = models.IntegerField()
    
    
class noall(models.Model):
    no = models.IntegerField() # 1 

    

    
    
    
    