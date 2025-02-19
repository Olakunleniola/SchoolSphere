from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    logo = models.ImageField(upload_to='school_logos/', null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    admin = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="school_admin"
    )

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name