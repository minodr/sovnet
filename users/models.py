from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        username = self.model.normalize_username(username)
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        user = self.create_user(username, email, password, **extra_fields)

        return user


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    public_key = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.BooleanField(default=True)

    profile_picture = models.URLField(blank=True, null=True)
    last_seen = models.DateTimeField(default=timezone.now)

    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return str(self.username)

    @property
    def is_online(self):
        threshold = timezone.now() - timezone.timedelta(minutes=1)
        return self.last_seen >= threshold
