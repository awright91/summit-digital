from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    service = models.CharField(max_length=250)
    url = models.URLField(null=True, blank=True)
    main_image = models.ImageField(upload_to = 'media/')
    hover_image = models.ImageField(upload_to = 'media/')



    def __str__(self):
        return self.title
