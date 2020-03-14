from django.contrib import admin

# Register your models here.
from src.status.models import Status

admin.site.register(Status)
