from django.db import models
from . import Base
from .post import PostBase

class Comment(PostBase, Base):
    posted_on = models.ForeignKey(PostBase, related_name='posted_on_%(class)s', on_delete=models.CASCADE) # it should be consider another comment too
    content = models.TextField(max_length=255)
    rate = models.BigIntegerField(default=0) # number of votes for this post
    # slug = models.SlugField(max_length=64, unique=True) # slug for links, removed seems unnecessary
    
    class Meta:
        ordering = ['-rate']
    