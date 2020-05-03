import os

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify

from django.urls import reverse

from . import models as images_models


def upload_path(instance, filename):

    now = timezone.now()
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/user_{}/{}/{}{}'.format(instance.user, now.strftime('%Y/%m/%d'), filename_base, filename_ext.lower())


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()

    image = models.ImageField(upload_to=upload_path)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    total_likes = models.PositiveIntegerField(db_index=True, default=0)  # used for denormalization

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
