from django.db import models

class post1(models.Model):  
    x1= models.IntegerField(blank=True,null=True)
    x2= models.CharField(max_length = 2,blank=True,null=True)
    #x2= models.FloatField(blank=True,null=True)
    x3= models.IntegerField(blank=True,null=True)  
    x4= models.IntegerField(blank=True,null=True)   

    def __str__(self):
        return str(self.x1)+","+str(self.x2)+ ","+str(self.x3)+","+str(self.x4)
 