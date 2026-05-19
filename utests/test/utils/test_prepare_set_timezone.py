from KeePassLibrary.base import datetime, timezone
from KeePassLibrary.utils import prepare_set_timezone
from KeePassLibrary.utils.data_types import TimeZone


def test_prepare_set_local_as_utc() -> None:
    time_local = datetime.now().replace(microsecond=0)
    time_local = time_local.astimezone(datetime.now().tzinfo)
    time_utc = datetime.now(timezone.utc).replace(microsecond=0)
    time_prepared = prepare_set_timezone(time_local, TimeZone.utc)
    assert time_prepared == time_utc


def test_prepare_set_utc_as_local() -> None:
    time_local = datetime.now().replace(microsecond=0)
    time_local = time_local.astimezone(datetime.now().tzinfo)
    time_utc = datetime.now(timezone.utc).replace(microsecond=0)
    time_prepared = prepare_set_timezone(time_utc, TimeZone.local)
    assert time_prepared == time_local


def test_prepare_set_none_as_local() -> None:
    time_none = datetime.now().replace(microsecond=0)
    time_local = time_none.astimezone(datetime.now().tzinfo)
    time_prepared = prepare_set_timezone(time_none, TimeZone.local)
    assert time_prepared == time_local


def test_prepare_set_none_as_utc() -> None:
    time_none = datetime.now().replace(microsecond=0)
    time_utc = time_none.astimezone(timezone.utc)
    time_prepared = prepare_set_timezone(time_none, TimeZone.utc)
    assert time_prepared == time_utc
