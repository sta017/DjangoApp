from django.db import models

# Create your models here.
class Insurance(models.Model):
   name = models.CharField(max_length=60)
   plan_type = models.CharField(max_length=60)
   death_benefits = models.CharField(max_length=60)
   payment_mode = models.CharField(max_length=60)
   sum_assured = models.CharField(max_length=60)

   def __str__(self):
      return self.name
