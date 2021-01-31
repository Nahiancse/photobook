from django.db import models
# from django.utils import timezone

# Create your models here.
class Photobook(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    description=models.TextField()
    published_date = models.DateField(blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.caption
