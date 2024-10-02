from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from petstagram.core.validators import alphabetical_validator


class AppUser(auth_models.AbstractUser):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    )
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            alphabetical_validator,
        ),

    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            alphabetical_validator,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    user_photo = models.ImageField(
        upload_to='profile_photos',
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=20,
        choices=CHOICES
    )

    @property
    def get_name(self):
        return f'{self.first_name} {self.last_name}'

