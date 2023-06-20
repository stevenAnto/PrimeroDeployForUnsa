from django.db import models
from . import Base, PostBase

class Comment(PostBase, Base):
    post = models.ForeignKey(PostBase, on_delete=models.CASCADE) # it should be consider another comment too
    # Content
    rate = models.BigIntegerField(default=0) # number of votes for this post
    slug = models.SlugField(max_length=64, unique=True) # slug for links
    
    class Meta:
        ordering = ['-rate']
    