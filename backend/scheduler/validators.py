import logging
from django.core.exceptions import ValidationError

logger = logging.getLogger('myLogger')


def validate_start_time(value):
        logger.critical(value)
        if value.minute != 0 or value.hour % 2 != 0:
        	raise ValidationError(u'%s is not a valid start time! Start time must be on the even hour.' % value)
