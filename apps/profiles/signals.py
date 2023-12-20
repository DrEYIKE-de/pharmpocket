# signals for creating profile after user save

import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.settings.base import AUTH_USER_MODEL
from .models import Profile


logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Save the user profile after signal received
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Save the user profile after signal received
    """
    instance.profile.save()
    logger.info("%s profile created ", instance)
