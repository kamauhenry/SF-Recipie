from django.db import models
from django.utils.text import slugify 
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from hitcount.models  import HitCountMixin, HitCount 
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager

User = get_user_model()
# Create your models here.

class Cook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length= 40, blank=True)
    slug = slug = models.SlugField(max_length=250, unique=True,blank=True)
    bio = HTMLField()
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.fullname
    
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.fullname)
        super(Cook, self).save(*args, **kwargs)

class Category (models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'categoriess'
    
    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    user = models.ForeignKey(Cook,  on_delete=models.CASCADE )
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False  )
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    tags =  TaggableManager()

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super(Post, self).save(*args, **kwargs)
