from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set.')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.full_clean()  # Optional: Ensure the user model is valid
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         if password is None:
#             raise TypeError('Superusers must have a password.')

#         return self.create_user(email, password, **extra_fields)
    

# class User(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=25, blank=True)
#     residence = models.CharField(max_length=255, blank=True)
#     gps_address = models.CharField(max_length=255, blank=True)
#     occupation = models.CharField(max_length=255, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(blank=True, null=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

#     class Meta:
#         verbose_name_plural = 'Users'


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=25)
    residence = models.CharField(max_length=255)
    gps_address = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255)
    date_registered = models.DateTimeField(default=timezone.now)