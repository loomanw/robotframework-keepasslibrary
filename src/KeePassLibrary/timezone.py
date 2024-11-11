# from datetime import datetime, timezone
from KeePassLibrary.base import datetime, timezone
from KeePassLibrary.errors import DateTimeInvalid, TimeZoneInvalid


def prepare_set_timezone(value: datetime, timez='UTC'):
    if not isinstance(value, datetime):
        raise DateTimeInvalid('Invalid DateTime object.')

    if not (timez == 'UTC') ^ (timez == 'local'):
        raise TimeZoneInvalid('Invalid timezone, expected UTC or local.')

    if value.tzinfo is None:
        value = add_datetime_timezone(value, timez)

    value = convert_datetime_timezone(value)

    return value


def add_datetime_timezone(value: datetime, timez='UTC'):
    if not (timez == 'UTC') ^ (timez == 'local'):
        raise TimeZoneInvalid('Invalid timezone, expected UTC or local.')

    if value.tzinfo is None:
        if timez == 'UTC':
            value = value.astimezone(timezone.utc)
        if timez == 'local':
            value = value.astimezone(datetime.now().tzinfo)

    return value


def convert_datetime_timezone(value: datetime, timez='UTC'):
    if not (timez == 'UTC') ^ (timez == 'local'):
        raise TimeZoneInvalid('Invalid timezone, expected UTC or local.')

    if value.tzname != timez:
        if timez == 'UTC':
            value = value.astimezone(timezone.utc)
        if timez == 'local':
            value = value.astimezone(datetime.now().tzinfo)

    return value
