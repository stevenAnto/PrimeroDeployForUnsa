from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from . import Base, Tag, Section
from .custom_user import CustomUser


class PostBase(Base):
    user = models.ForeignKey(User, on_delete=models.SET(CustomUser.get_deleted_user)) # if User deleted set certain User
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class PostType(Base):
    name = models.CharField(max_length=64, unique=True)
    
    class Meta:
        ordering = ['name']
        
    def get_default_type():
        return PostType.objects.get_or_create(name='Default type')[0].id

class Post(PostBase, Base):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=255, blank=True)
    img = models.ImageField(upload_to='posts', blank=True) 
    file = models.FileField(upload_to='posts', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET_DEFAULT, default=Section.get_default_section) # If deleted section, then set default
    post_type = models.ForeignKey(PostType, on_delete=models.SET_DEFAULT, default=PostType.get_default_type) # To MODIFY in MODEL
    rate = models.BigIntegerField(default=0) # number of votes for this post
    slug = models.SlugField(max_length=64, unique=True, editable=False) # slug for links
    
    class Meta:
        ordering = ['-rate']
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    