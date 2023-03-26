from django.db import models
from django.utils.text import slugify 
from django.contrib.auth import get_user_model




User = get_user_model()
# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    fullname = models.CharField(max_length= 40, blank=true)
    slug = slug = models.SlugField(max_length=400, unique=True,blank=True)
    bio = models.TextField()
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.fullname)
        super(Post, self).save(*args, **kwargs)


class Post(models.Model):
    title =models.Charfield(max_length=350)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey()

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super(Post, self).save(*args, **kwargs)
