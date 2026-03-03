from django.core.exceptions import ValidationError


def validation_license_number(license_number: str) -> str:
    MAX_LENGTH = 8

    if len(license_number) != MAX_LENGTH:
        raise ValidationError("Number of driver license must be 8 chars")

    if (license_number[:3] != license_number[:3].upper() or
            not all(item.isalpha() for item in license_number[:3])):
        raise ValidationError("First 3 chars must be upper case")

    if not all(item.isdigit() for item in license_number[3:]):
        raise ValidationError("Last 5 chars must be digits")

    return license_number
