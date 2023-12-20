from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


class UserManager (BaseUserManager):
    def validate_email(self, email):
        try:
            EmailValidator(email)
        except ValidationError:
            raise ValueError(_("This email is not valid"))
                       
    def create_user(self, username, email, password, phone_number, **extra_fields):    
        if not username:
            raise ValueError(_("Users must provide a username"))    
        if not phone_number:
            raise ValueError(_("Base_User: Users must provide a phone_number"))     
        if email:
            email = self.normalize_email(email)
            self.validate_email(email)
        else:
            raise ValueError(_("User must provide a valid and correct email"))
              
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        
        user = self.model(username=username, email=email, phone_number=phone_number, **extra_fields)
        
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, username, email, password, phone_number, **extra_fields):
        
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Super_User need is_superuser parameter on True"))
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Super_User need is_staff parameter on True"))
        
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Super_User need is_active parameter on True"))
        
        if email:
            email = self.normalize_email(email)
            self.validate_email(email)
        else:
            raise ValueError(_("User must provide a valid and correct email"))
               
        user = self.create_user(username=username, email=email,
                                password=password, phone_number=phone_number, **extra_fields)
        user.save(using=self._db)
        return user