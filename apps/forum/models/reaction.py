from django.db import models
from . import Base

class Reaction(Base):
    description = models.CharField(max_length=255, unique=True)
    
    def get_default_reaction():
        return Reaction.objects.get_or_create(description="Default reaction if it's deleted")[0]
    