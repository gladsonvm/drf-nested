from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    add_info = models.CharField(null=True, blank=True, max_length=100)
    user = models.OneToOneField(User)


class nestedmodel(models.Model):
    info = models.CharField(null=True, blank=True, max_length=100)
    user = models.ForeignKey(User)
    profile = models.ForeignKey(UserProfile)


