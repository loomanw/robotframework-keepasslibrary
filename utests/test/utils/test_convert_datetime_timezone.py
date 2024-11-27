from KeePassLibrary.base import datetime, timezone, timedelta
from KeePassLibrary.utils import TimeZoneInvalid
from KeePassLibrary.utils import convert_datetime_timezone


def test_convert_datetime_to_utc():
    time_delta6 = datetime.now(timezone(offset=timedelta(hours=6))).replace(microsecond=0)
    time_utc = datetime.now(timezone.utc).replace(microsecond=0)
    time_converted = convert_datetime_timezone(time_delta6, 'UTC')
    assert time_converted == time_utc


def test_convert_datetime_to_local():
    time_delta6 = datetime.now(timezone(offset=timedelta(hours=6))).replace(microsecond=0)
    time_local = datetime.now().replace(microsecond=0)
    time_local = time_local.astimezone(datetime.now().tzinfo)
    time_converted = convert_datetime_timezone(time_delta6, 'local')
    assert time_converted == time_local


def test_convert_datetime_timezone_invalid():
    try:
        time_utc = datetime.now(timezone.utc).replace(microsecond=0)
        time_converted = convert_datetime_timezone(time_utc, 'fake timezone')  # noqa: F841
        assert False
    except TimeZoneInvalid:
        assert True
