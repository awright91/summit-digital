from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'media/')
    description = RichTextField()
    pub_date = models.DateTimeField()


    def __str__(self):
        return self.title


    def summary(self):
        return self.description[:250] + '...'

    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs = {'post_id': self.id, 'slug': self.slug()})

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
