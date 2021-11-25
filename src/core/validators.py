from django.core.exceptions import ValidationError


def validate_email_for_prohibited_domain(value):

    BLACKLIST = ['zzz.com']

    _, _, email_domain = value.partition('@')

    if email_domain in BLACKLIST:
        raise ValidationError('Prohibited domain')

    return value