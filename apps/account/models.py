from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.db import models

class UserManager(BaseUserManager):
    """
    Custom manager for custome User to handle user creation with email instead of username.
    """
    def create_user(self, username, email, name, role, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set.")
        if not name:
            raise ValueError("The Name field must be set.")
        if not role:
            raise ValueError("The Role field must be set.")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, name=name, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, role, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")
        
        username = email.split('@')[0] 
        return self.create_user(username, email, name, role, password, **extra_fields)


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=255, null=False)
    ROLE_CHOICES = [
        ("student", 'Student'),
        ("admin", 'Admin'),
        ("teacher", 'Teacher'),
        ("parent", 'Parent')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)

    # Additional fields for admin support if needed
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'role']

    objects = UserManager()

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"