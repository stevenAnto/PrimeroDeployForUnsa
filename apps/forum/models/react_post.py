from django.db import models
from django.contrib.auth.models import User
from . import Base, PostBase, Reaction

class ReacPost(Base):
    post = models.ForeignKey(PostBase, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_reaction = models.ForeignKey(Reaction, on_delete=models.SET(Reaction.get_default_reaction))
    
    class Meta:
        ordering = ['-post']
        unique_together = ('post', 'user')
        