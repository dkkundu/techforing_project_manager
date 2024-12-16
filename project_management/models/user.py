from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(
        Group,
        related_name="project_management_user_set",  # Custom related name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="project_management_user_permissions_set",  # Custom related name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username
