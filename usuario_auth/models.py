from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    groups = models.ManyToManyField(
    'auth.Group',
    verbose_name='groups',
    blank=True,
    help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    related_name="customuser_groups",
    related_query_name="customuser",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",
        related_query_name="customuser",
    )

    @property
    def age(self):
        if self.date_of_birth is None:
            return None
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))