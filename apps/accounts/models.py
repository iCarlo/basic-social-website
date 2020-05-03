import os

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


def upload_path(instance, filename):
    now = timezone.now()
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/user_{}/{}/{}{}'.format(instance.user, now.strftime('%Y/%m/%d'), filename_base, filename_ext.lower())


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=upload_path, blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Contact(models.Model):  # intermidiate(intermediary) model for ManyToManyField
    user_from = models.ForeignKey(  # Model having a ManyToManyField relationship with a Source Model
        'auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(    # a Source Model making a ManyToManyField relationship
        'auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


# add following field to User dyanmically
User.add_to_class('following', models.ManyToManyField(
    'self', through=Contact, related_name='followers', symmetrical=False))
