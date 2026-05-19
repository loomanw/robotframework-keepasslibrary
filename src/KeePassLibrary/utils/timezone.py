from KeePassLibrary.base import datetime, timezone
from KeePassLibrary.utils.data_types import TimeZone


def prepare_set_timezone(value: datetime, timez: TimeZone = TimeZone.utc) -> datetime:

    if value.tzinfo is None:
        value = add_datetime_timezone(value, timez)

    value = convert_datetime_timezone(value)

    return value


def add_datetime_timezone(value: datetime, timez: TimeZone = TimeZone.utc) -> datetime:

    if value.tzinfo is None:
        if timez == TimeZone.utc:
            value = value.astimezone(timezone.utc)
        if timez == TimeZone.local:
            value = value.astimezone(datetime.now().tzinfo)

    return value


def convert_datetime_timezone(value: datetime, timez: TimeZone = TimeZone.utc) -> datetime:

    if value.tzname != timez:
        if timez == TimeZone.utc:
            value = value.astimezone(timezone.utc)
        if timez == TimeZone.local:
            value = value.astimezone(datetime.now().tzinfo)

    return value
