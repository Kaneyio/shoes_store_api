from django.db import models

class Attributes(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.name}"
  
class ShoeType(models.Model):
  name = models.CharField(max_length=255)
  attributes = models.ManyToManyField(Attributes, blank=True)

  def __str__(self):
    return self.name

class Shoe(models.Model):
  name = models.CharField(max_length=255)
  shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
  price = models.IntegerField()

  def __str__(self):
    return self.name