from django.db import models
from . import Base, PostBase

class Comment(PostBase, Base):
    post = models.ForeignKey(PostBase, on_delete=models.CASCADE) 
    # Content
    rate = models.BigIntegerField(default=0) # number of votes for this post
    slug = models.SlugField(max_length=64, unique=True) # slug for links
    
    class Meta:
        ordering = ['name']
        
    def get_default_section():
        return Section.objects.get_or_create(name='No Section')[0]
    