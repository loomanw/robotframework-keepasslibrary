from enum import Enum


class TimeZone(Enum):
    """Enum that defines timezone to use."""
    utc = "UTC"
    local = "local"
