from django.conf import settings
from django.db import models


def upload_to(instance, filename):
    return 'updates/{user}/{filename}'.format(user=instance.user.username, filename=filename)


# Create your models here.
class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""
