from django.db import models

# Create your models here.
class FashionFile(models.Model):
    file_name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.file_name + ' ' + self.type
