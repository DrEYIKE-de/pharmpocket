from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _ 
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager


class User (AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(editable=False, unique=True, default=uuid.uuid4, )
    username = models.CharField(max_length=255, unique=True, verbose_name=_("Your username"), 
                                help_text=_("add your username"),)
    email = models.EmailField(max_length=50, unique=True, verbose_name=_("Your email"),)
    phone_number = PhoneNumberField(region="CM", default="+237695408607",)
    is_active = models.BooleanField(default=False, verbose_name=_("Is this user active"),)
    is_superuser = models.BooleanField(default=False, verbose_name=_("Is this user superuser"),)
    is_staff = models.BooleanField(default=False, verbose_name=_("Is this user in staff"),)
    date_joined = models.DateTimeField(auto_now_add=True, )
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number", "email"]
    
    objects = UserManager()
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        
    def __str__(self):
        return self.username 
    
    @property
    def get_short_name(self):
        return self.username
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_full_info(self):
        return f"name : {self.username.title()}, email: {self.email}, number: {self.phone_number}"
    
