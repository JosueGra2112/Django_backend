from django.db import models

class RadioStation(models.Model):
    title = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    call_sign = models.CharField(max_length=20)
    slogan = models.CharField(max_length=100)
    streaming_url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='', blank=True, null=True) 
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
