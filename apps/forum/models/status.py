from django.db import models
from . import Base

class Status(Base):
    description = models.CharField(max_length=255, unique=True)
    
    def get_default_status():
        Status.objects.get_or_create(description='Default status')[0]
    