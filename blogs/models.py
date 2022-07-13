from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=400, null=True)
    slug = AutoSlugField(populate_from='title')
    image = models.FileField(upload_to='blogs')
    description = models.TextField(null=True)
    snippet = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.title