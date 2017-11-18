from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

#unused
def validate_keynum(value):
    if value < 0 or value > 9999:
        raise ValidationError(
            _('%(value)s must be between 0 and 9999.'),
            params={'value': value},
        )