from django.db import models
from . import Base

class Status(Base):
    description = models.CharField(max_length=255, unique=True) # problems with implement this model(i. e. active inactive and banned)
    
    def get_default_status():
        return Status.objects.get_or_create(description='Default status')[0]
    