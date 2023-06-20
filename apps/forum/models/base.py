from django.db import models

class Base(models.Model):
    STATE_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('X', 'Deleted'),
    )
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='A')