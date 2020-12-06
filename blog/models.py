from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_date  = models.DateTimeField(default=timezone.now)
    post_text  = models.CharField(max_length=300)
    post_image = models.ImageField(upload_to='event_images/')

