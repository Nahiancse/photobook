from django.db import models

# Create your models here.
class Photobook(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    description=models.TextField()

    def __str__(self):
        return self.caption
