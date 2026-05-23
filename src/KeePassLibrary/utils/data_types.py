import re
from enum import Enum
from KeePassLibrary.base import Entry, Group
from KeePassLibrary.errors import RegExpFlagsInvalid


class TimeZone(Enum):
    """Enum that defines timezone to use."""
    utc = "UTC"
    local = "local"


class RegExpFlags(str):
    @classmethod
    def from_string(cls, string: str) -> "RegExpFlags":
        """Set

        Following flags are supported:
        | =Flag= | =Description= |
        | g | Global search. |
        | i | Case-insensitive search. |
        | m | Allows ``^`` and ``$`` to match newline characters. |
        | s | Allows ``.`` to match newline characters. |
        | u | "unicode"; treat a pattern as a sequence of unicode code points. |
        | y | Perform a "sticky" search that matches starting at the current position in the target string. |

        See [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp|RegExp Object]
        and [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions|RegExp Guide] for more information.
        """
        match = re.fullmatch(r'^[gimsuy]+', string)
        if not match:
            raise RegExpFlagsInvalid('Invalid RegExp flags.')
        return cls(string)


def keepass_entry(entry: Entry) -> Entry:
    """Each `Entry` contains all the information stored for a website or application

    | = Attribute = |
    | title         |
    | username      |
    | password      |
    | url           |
    | tags          |
    | icon          |
    | parent_group  |
    | uuid          |
    | expires       |
    | expired       |
    | path          |
    """
    return entry


def keepass_group(group: Group) -> Group:
    """Each `Group` may contain 1 or more Groups or Entries

    | = Attribute = |
    | name          |
    | notes         |
    | entries       |
    | subgroups     |
    | is_root_group |
    | icon          |
    | parent_group  |
    | uuid          |
    | expires       |
    | expired       |
    | path          |
    """
    return group
