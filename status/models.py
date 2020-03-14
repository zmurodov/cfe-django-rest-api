from django.conf import settings
from django.db import models


def upload_to(instance, filename):
    return "upload/{username}/{filename}".format(username=instance.user.username, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):

    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


# Create your models here.
class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)[:50]
