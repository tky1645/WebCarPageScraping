from django.db import models

# Create your models here.
class BikeInfo(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    
    #追加
    price = models.CharField(max_length=100,default='****')
    distance = models.CharField(max_length=100,default='****')
    URL = models.URLField(default='https://www.google.com/')


    def __str__(self):
        return self.title
    
    #登録処理（SQLiteなのでそのままSave()でOK）
    def CreateorUpdate(self):
        self.save()
    


        

