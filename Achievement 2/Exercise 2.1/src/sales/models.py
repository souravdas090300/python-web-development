from django.db import models


# Create your models here.
class Sale (models.Model):
    name = models.CharField(max_length=120)
    notes = models.TextField()
    pic = models.ImageField(upload_to='sales', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)