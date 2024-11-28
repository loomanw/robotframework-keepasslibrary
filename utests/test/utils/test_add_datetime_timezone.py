from KeePassLibrary.base import datetime, timezone, timedelta
from KeePassLibrary.utils import TimeZoneInvalid
from KeePassLibrary.utils import add_datetime_timezone


def test_add_datetime_timezone_utc():
    time_orig = datetime.now().replace(microsecond=0)
    time_utc = time_orig.astimezone(timezone.utc)
    time_converted = add_datetime_timezone(time_utc, 'local')
    assert time_utc == time_converted


def test_add_datetime_timezone_local():
    time_orig = datetime.now().replace(microsecond=0)
    time_local = time_orig.astimezone(datetime.now().tzinfo)
    time_converted = add_datetime_timezone(time_orig, 'local')
    assert time_local == time_converted


def test_add_datetime_timezone_skip_none():
    time_delta6 = datetime.now(timezone(offset=timedelta(hours=6))).replace(microsecond=0)
    time_converted = add_datetime_timezone(time_delta6, 'UTC')
    assert time_delta6 == time_converted


def test_add_datetime_timezone_timezone_invalid():
    try:
        time_utc = datetime.now(timezone.utc).replace(microsecond=0)
        time_add_zone = add_datetime_timezone(time_utc, 'fake timezone')  # noqa: F841
        assert False
    except TimeZoneInvalid:
        assert True
