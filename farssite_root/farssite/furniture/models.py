import os
import uuid
import datetime

from django.db import models
from django.conf import settings
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Furniture(models.Model):
    """Model representing a specific picture."""
    TYPE = (
        ('table', 'Bord'),
        ('stump', 'Stubbe'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    uploaded = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    title = models.CharField(max_length=100, blank=False)
    piece = models.CharField(max_length=32, choices=TYPE, null=True)
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d',
        height_field=None,
        width_field=None,
        max_length=100,
        null=True,
    )
    description = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return f'{self.piece}, created {self.uploaded}'

    def get_absolute_url(self):
        return reverse('furniture-detail', args=[str(self.id)])
