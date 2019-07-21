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
    type = models.CharField(choices=FASHION_TYPE, max_length=200)

    def __str__(self):
        return self.file_name + ' ' + self.type

class TrainedModel(models.Model):
    file_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
