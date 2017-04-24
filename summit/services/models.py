from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length = 250)
    icon = models.ImageField(upload_to = 'media/')
    description = models.TextField()
    tagline = models.CharField(max_length=400, default='')
    reason_1_title = models.CharField(max_length=250, default='')
    reason_1_description = models.TextField(default='')
    reason_2_title = models.CharField(max_length=250, default='')
    reason_2_description = models.TextField(default='')
    reason_3_title = models.CharField(max_length=250, default='')
    reason_3_description = models.TextField(default='')
    reason_4_title = models.CharField(max_length=250, default='')
    reason_4_description = models.TextField(default='')


    def __str__(self):
        return self.title


    def summary(self):
        return self.description[:250] + '...'

    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs = {'service_id': self.id, 'slug': self.slug()})
