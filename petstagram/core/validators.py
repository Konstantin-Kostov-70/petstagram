from django.core import validators


def alphabetical_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise validators.ValidationError('name  must contain only alphabetical letters')