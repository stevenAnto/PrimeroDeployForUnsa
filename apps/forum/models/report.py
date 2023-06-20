from django.db import models
from django.contrib.auth.models import User
from . import Base, BasePost

class Report(Base):
    post = models.ForeignKey(BasePost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.TextField(max_length=1024)
    slug = models.SlugField(max_length=64, unique=True) # slug for links
    
    class Meta:
        ordering = ['-post']
        