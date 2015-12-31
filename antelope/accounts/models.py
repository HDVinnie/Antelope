from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from random import choice
from string import ascii_lowercase, digits

class AntelopeUserManager(BaseUserManager):
    def create_user(self, username, password, email):
        if not username:
            raise ValueError('Users must have a username')

        if not email:
            raise ValueError('Users must have an email')

        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            username=username,
            email=self.normalize_email(email), 
            passkey=''.join(choice(ascii_lowercase + digits) for _ in range(32))
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username, 
            password=password, 
            email=email
        )

        user.is_admin = True
        user.save(using=self._db)

        return user

class AntelopeUser(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255)
    passkey = models.CharField(max_length=32)
    joined_date = models.DateField(auto_now_add=True)
    
    uploaded = models.BigIntegerField(default=0)
    downloaded = models.BigIntegerField(default=0)
    torrents_uploaded = models.PositiveIntegerField(default=0)
    torrents_downloaded = models.PositiveIntegerField(default=0)

    invites = models.IntegerField(default=0)
    can_invite = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AntelopeUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        # TODO : Update this when member classes are added
        return True

    def has_module_perms(self, app):
        # TODO : Update this when member classes are added
        return True

    @property
    def is_staff(self):
        # TODO : Update this when member classes are added
        return self.is_admin

class UserLogin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    login = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.user.username
