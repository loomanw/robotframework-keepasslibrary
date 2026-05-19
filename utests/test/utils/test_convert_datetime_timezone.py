from KeePassLibrary.base import datetime, timezone, timedelta
from KeePassLibrary.utils import convert_datetime_timezone
from KeePassLibrary.utils.data_types import TimeZone


def test_convert_datetime_to_utc() -> None:
    time_delta6 = datetime.now(timezone(offset=timedelta(hours=6))).replace(microsecond=0)
    time_utc = datetime.now(timezone.utc).replace(microsecond=0)
    time_converted = convert_datetime_timezone(time_delta6, TimeZone.utc)
    assert time_converted == time_utc


def test_convert_datetime_to_local() -> None:
    time_delta6 = datetime.now(timezone(offset=timedelta(hours=6))).replace(microsecond=0)
    time_local = datetime.now().replace(microsecond=0)
    time_local = time_local.astimezone(datetime.now().tzinfo)
    time_converted = convert_datetime_timezone(time_delta6, TimeZone.local)
    assert time_converted == time_local
