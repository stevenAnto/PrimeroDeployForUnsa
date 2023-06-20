from django.db import models
from django.contrib.auth.models import User
from . import Base, CustomUser, Tag, Section, PostType

class Post(Base):
    user = models.ForeignKey(User, on_delete=models.SET(CustomUser.get_deleted_user)) # if User deleted set certain User
    title = models.CharField(max_length=128, blank=True) 
    img = models.ImageField(upload_to='posts') 
    file = models.FileField(upload_to='posts')
    tags = models.ManyToManyField(Tag, blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET_DEFAULT, default=Section.get_default_section) # If deleted section, then set default
    post_type = models.ForeignKey(PostType, on_delete=models.SET_NULL, null=True) 
    rate = models.BigIntegerField(default=0) # number of votes for this post
    slug = models.SlugField(max_length=64, unique=True) # slug for links
    
    class Meta:
        ordering = ['-rate']
    