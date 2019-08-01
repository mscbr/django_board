from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPostQueryset(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

class BoardPostManager(models.Manager):
    def get_queryset(self):
         return BlogPostQueryset(self.model, using=self._db)

class BoardPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.FileField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BoardPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/board/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url()}/edit/"
    
    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete/"
   