from django.db import models

    
class outpass(models.Model):
    name=models.CharField(max_length=20)
    plf=models.CharField(max_length=20)
    date=models.DateField(auto_now_add='True')
    time=models.TimeField(auto_now_add='True')

class outing(models.Model):
    name=models.CharField(max_length=20)
    plf=models.CharField(max_length=20)
    date=models.DateField(auto_now_add='True')
    time=models.TimeField(auto_now_add='True')

class amiclean(models.Model):
    name=models.CharField(max_length=20)
    plf=models.CharField(max_length=20)
    des=models.CharField(max_length=100)
    date=models.DateField(auto_now_add='True')
    time=models.TimeField(auto_now_add='True')
