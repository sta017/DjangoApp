from django.db import models

# Create your models here.
class Data(models.Model):
  Name = models.CharField(max_length=60)
  Value= models.CharField(max_length=60)

  def __str__(self):
     return self.name
