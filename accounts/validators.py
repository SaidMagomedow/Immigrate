import os
from django.core.exceptions import ValidationError


def validate_image_extension(value):
    allowed_extensions = ('.png', '.jpeg', '.jpg', '.gif', 'webp')
    if os.path.splitext(value.name)[1] not in allowed_extensions:
        raise ValidationError('Неверный формат загружаемой картинки.')
    return value