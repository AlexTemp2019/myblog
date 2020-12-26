from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=300)
    image = models.ImageField(upload_to='event_images/')
