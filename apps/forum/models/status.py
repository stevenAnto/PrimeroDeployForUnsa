from django.db import models
from . import Base

class Status(Base):
    description = models.CharField(max_length=255, unique=True)
    
    class Meta:
        ordering = ['name']
    