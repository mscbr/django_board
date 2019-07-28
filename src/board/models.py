from django.db import models

# Create your models here.

class BoardPost(models.Model):
    # id = models.IntegerField() as default
    title = models.TextField()
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title