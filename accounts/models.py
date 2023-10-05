from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UsersManager


class Users(AbstractBaseUser):
    full_name = models.CharField(_('full name'), max_length=100)
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    mobile_phone = models.CharField(_('mobile phone'), max_length=100)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    
    objects = UsersManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('mobile_phone', 'full_name')
    
    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_admin(self):
        return self.is_staff
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'