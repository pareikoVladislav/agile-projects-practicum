from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from projects.choices import Positions
from projects.models.project import Project


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    position = models.CharField(
        _('position'),
        max_length=30,
        choices=Positions.choices(),
    )
    projects = models.ManyToManyField(Project, related_name="staff")
    date_joined = models.DateTimeField(default=timezone.now)
    birth_date = models.DateField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'position']

    def __str__(self):
        return self.email
