import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.
def user_cv_file_path(instance, filename):
    """Generate file path for new recipe cv file"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/cv/", filename)


class UserManager(BaseUserManager):
    def create_user(
            self,
            email: str,
            password: str = None,
            **extra_fields: dict,
    ) -> object:
        """Creates and saves a new user"""
        if not email:
            raise ValueError("users must have email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        """Create and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False, )
    cv = models.FileField(null=True, upload_to=user_cv_file_path)
    objects = UserManager()
    USERNAME_FIELD = "email"
