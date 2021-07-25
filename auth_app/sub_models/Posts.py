'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''
from djongo import models

class Posts(models.Model):
    PostId=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=200)
    Image=models.BinaryField()
    Descripton=models.CharField(max_length=200)
    DatePosted=models.DateTimeField()