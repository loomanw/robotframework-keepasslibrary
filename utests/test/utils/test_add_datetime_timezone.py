from KeePassLibrary.base import datetime, timezone, timedelta
from KeePassLibrary.utils import add_datetime_timezone
from KeePassLibrary.utils.data_types import TimeZone


def test_add_datetime_timezone_utc() -> None:
    time_orig = datetime.now().replace(microsecond=0)
    time_utc = time_orig.astimezone(timezone.utc)
    time_converted = add_datetime_timezone(time_utc, TimeZone.local)
    assert time_utc == time_converted


def test_add_datetime_timezone_local() -> None:
    time_orig = datetime.now().replace(microsecond=0)
    time_local = time_orig.astimezone(datetime.now().tzinfo)
    time_converted = add_datetime_timezone(time_orig, TimeZone.local)
    assert time_local == time_converted


def test_add_datetime_timezone_skip_none() -> None:
    time_delta6 = datetime.now(timezone(offset=timedelta(hours=6))).replace(microsecond=0)
    time_converted = add_datetime_timezone(time_delta6, TimeZone.utc)
    assert time_delta6 == time_converted
