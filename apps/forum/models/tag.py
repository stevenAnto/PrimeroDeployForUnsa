from django.db import models
from . import Base

class Tag(Base):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True, primary_key=True) # slug for links
    
    class Meta:
        ordering = ['name']
    