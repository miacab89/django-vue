from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, UserManager
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self.d)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email, password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser):
    # pass

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def _str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profiles-images')
    fb_profile = models.CharField(max_length=100)
    twitter_profile = models.CharField(max_length=100)
    linkedin_profile = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

