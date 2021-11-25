import re
from django.core.exceptions import ValidationError


def validate_email_for_prohibited_domain(value):

    BLACKLIST = ['zzz.com']

    _, _, email_domain = value.partition('@')

    if email_domain in BLACKLIST:
        raise ValidationError('Prohibited domain')

    return value


def validate_phone(value):
    SHORT_LENGTH = 13  # noqa

    phone_number = value

    pattern = '(\(\d\d\d\)|\+\d\d\(\d\d\d\))\d\d\d\-\d\d\d\d'  # noqa

    if not re.match(pattern, phone_number):
        raise ValidationError('Phone number is not correct')

    return value
