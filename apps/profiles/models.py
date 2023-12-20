# Profile user models

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.utils.models import ModelsUtils

User = get_user_model()


class GenderTypes(models.TextChoices):
    """
    Gender for all the users
    """

    MALE = "MALE", _("MALE")
    FEMALE = "FEMALE", _("FEMALE")
    OTHER = "OTHER", _("OTHER")


class UserTypes(models.TextChoices):
    """
    User title for Users
    """

    DOCTOR = "DOCTOR", _("DOCTOR")
    PROFESSOR = "PROFESSOR", _("PROFESSOR")
    PHARMACY_HELPER = "PHARMACY_HELPER", _("PHARMACY_HELPER")
    PATIENT = "PATIENT", _("PATIENT")


class Profile(ModelsUtils):
    """
    Profile model for User
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_("user"), related_name="profile"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=255,
        choices=GenderTypes.choices,
        default=GenderTypes.OTHER,
    )
    title = models.CharField(
        verbose_name=("Your user Grade"),
        max_length=100,
        choices=UserTypes.choices,
        default=UserTypes.PATIENT,
    )
    profile_photo = models.ImageField(
        upload_to="profiles/",
        default="profile_photo.png",
        verbose_name=_("your profile photo"),
    )
    biography = models.TextField(
        default=_("Tells us more about you"), verbose_name=_("your biography")
    )
    is_employee = models.BooleanField(
        default=False,
        help_text=_("determine if this user an employee"),
        verbose_name=_("is an employee"),
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return f"{self.user.username.title()} 's profile created"
