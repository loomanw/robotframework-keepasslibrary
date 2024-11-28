from KeePassLibrary.base import datetime, timezone
from KeePassLibrary.utils import TimeZoneInvalid, DateTimeInvalid
from KeePassLibrary.utils import prepare_set_timezone


def test_prepare_set_local_as_utc():
    time_local = datetime.now().replace(microsecond=0)
    time_local = time_local.astimezone(datetime.now().tzinfo)
    time_utc = datetime.now(timezone.utc).replace(microsecond=0)
    time_prepared = prepare_set_timezone(time_local, 'UTC')
    assert time_prepared == time_utc


def test_prepare_set_utc_as_local():
    time_local = datetime.now().replace(microsecond=0)
    time_local = time_local.astimezone(datetime.now().tzinfo)
    time_utc = datetime.now(timezone.utc).replace(microsecond=0)
    time_prepared = prepare_set_timezone(time_utc, 'local')
    assert time_prepared == time_local


def test_prepare_set_none_as_local():
    time_none = datetime.now().replace(microsecond=0)
    time_local = time_none.astimezone(datetime.now().tzinfo)
    time_prepared = prepare_set_timezone(time_none, 'local')
    assert time_prepared == time_local


def test_prepare_set_none_as_utc():
    time_none = datetime.now().replace(microsecond=0)
    time_utc = time_none.astimezone(timezone.utc)
    time_prepared = prepare_set_timezone(time_none, 'UTC')
    assert time_prepared == time_utc


def test_prepare_set_timez_value_invalid():
    try:
        time_flaseutc = True
        time_converted = prepare_set_timezone(time_flaseutc, 'UTC')  # noqa: F841
        assert False
    except DateTimeInvalid:
        assert True


def test_prepare_set_timez_timez_invalid():
    try:
        time_utc = datetime.now(timezone.utc).replace(microsecond=0)
        time_converted = prepare_set_timezone(time_utc, 'fake timezone')  # noqa: F841
        assert False
    except TimeZoneInvalid:
        assert True
