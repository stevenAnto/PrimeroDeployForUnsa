from django.db import models
from django.contrib.auth.models import User
from . import Base, PostBase, Tag, Section, PostType

class Post(PostBase, Base):
    title = models.CharField(max_length=128, blank=True)
    content = models.TextField(max_length=255)
    img = models.ImageField(upload_to='posts') 
    file = models.FileField(upload_to='posts')
    tags = models.ManyToManyField(Tag, blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET_DEFAULT, default=Section.get_default_section) # If deleted section, then set default
    post_type = models.ForeignKey(PostType, on_delete=models.SET_NULL, null=True) # To MODIFY in MODEL
    rate = models.BigIntegerField(default=0) # number of votes for this post
    slug = models.SlugField(max_length=64, unique=True) # slug for links
    
    class Meta:
        ordering = ['-rate']
    