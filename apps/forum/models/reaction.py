from django.db import models
from . import Base

class Reaction(Base):
    description = models.CharField(max_length=255, unique=True)
    