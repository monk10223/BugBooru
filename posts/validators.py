import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

TAG_PATTERN = re.compile(r'^[a-z_]+$')
MAX_TAGS = 30
MAX_TAG_LENGTH = 100


validate_image_url = RegexValidator(
    regex=r'\.(jpe?g|png|gif|webp)(\?.*)?$',
    message='URL must point to an image (jpg, png, gif, webp).',
    flags=re.IGNORECASE,
)


def validate_tags(tags):
    if len(tags) > MAX_TAGS:
        raise ValidationError(f'Use at most {MAX_TAGS} tags.')
    for tag in tags:
        if len(tag) > MAX_TAG_LENGTH:
            raise ValidationError(f'Tag "{tag[:20]}..." is too long.')
        if not TAG_PATTERN.match(tag):
            raise ValidationError(
                f'Tag "{tag}" is invalid. Use only letters and underscores.'
            )