from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_agent = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ServicingGroup(models.Model):
    """
        Preserves data
    """
    pass


class Group(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    mnemonic = models.CharField(max_length=50, null=False, blank=False,
                                default="")
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children',
                               on_delete=models.SET_NULL)


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Permission(models.Model):
    pass


class PermissionSet(models.Model):
    pass


class CustomField(models.Model):
    pass


class SystemProperty(models.Model):
    """
        Contains various system properties for use i.e. for in-place upgrade.
    """
    key = models.CharField(max_length=500, null=False, blank=False)
    value = models.CharField(max_length=5000, null=True, blank=True)
