from django.db import models
from . import Base

class PostType(Base):
    name = models.CharField(max_length=64, unique=True)
    
    class Meta:
        ordering = ['name']
    