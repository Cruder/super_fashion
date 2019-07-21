from django.db import models
from enum import Enum

FASHION_TYPE= (   # A subclass of Enum
    ('0', "T-shirt/top"),
    ('1', "Trouser"),
    ('2', "Pullover"),
    ('3', "Dress"),
    ('4', "Coat"),
    ('5', "Sandal"),
    ('6', "Shirt"),
    ('7', "Sneaker"),
    ('8', "Bag"),
    ('9', "Ankle boot")
)

# Create your models here.
class FashionFile(models.Model):
    file_name = models.CharField(max_length=200)

class TrainedModel(models.Model):
    file_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Result(models.Model):
    fashion_file = models.ForeignKey('FashionFile', on_delete=models.CASCADE)
    trained_model = models.ForeignKey('TrainedModel', on_delete=models.CASCADE)
    type = models.CharField(choices=FASHION_TYPE, max_length=200)
