from django.db import models

# Create your models here.
class BikeInfo(models.Model):
    title = models.CharField(max_length=100)
    year = models.TextField()

    def __str__(self):
        return self.title
        

