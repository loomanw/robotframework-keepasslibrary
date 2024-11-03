from robotlibcore import DynamicCore

from KeePassLibrary.keywords import (
    KeePassDatabase,
    KeePassEntry,
    KeePassEntries,
    KeePassGroup,
    KeePassGroups
)

__version__ = '0.5.0'

class KeePassLibrary(DynamicCore):
    """KeePassLibrary is a library for Robot Framework.
    
    KeePassLibrary uses the PyKeePass modules internally to access KeePass databases
    
    See https://keepass.info for more information about KeePass in general.

    == Table of contents ==
    
    %TOC%
    
    = Databases =
    
    The following databases are supported;
    - KDBX3 (3.1)
    - KDBX4 (4.0)
    
    https://keepass.info/help/kb/kdbx_4.html 
    
    Example:
    | `Load Keepass Database` | Database.kdbx | Database.key | #Load a Keepass database named Database.kdbx using the keyfile Database.key |       

    = Entries and Groups =
    
    A KeePass database (KDBX) is a tree of Groups, each Goup can contain multiple Groups and Entries

    == Entry ==
    
    Entries can be found using the `Get Entries` like keywords to return a single Entry or list of Entries.
    
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
    
    == Group ==
    
    Groups can be found using the `Get Groups` like keywords to return a single Group or list of Groups.
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
    
    = Regular expression =
    
    When ``regex`` is set to True the supplied string is matched using regular expression:
    - https://docs.python.org/3/library/re.html#re-syntax
    - https://docs.python.org/3/howto/regex.html#regex-howto
    
    == Flags ==
    
    When ``regex`` is set to True a combination of ``flags`` can be set: 
    | =Flag= | =Short Desciption= | =Long description= |
    | i      | Ignore case        | Perform case-insensitive matching. |
    | m      | Multiline          | Make begin/end {^, $} consider each line. |
    | s      | Dotall             | Makes the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline. |
    | l      | Locale             | Make {\w, \W, \b, \B} follow locale. |
    | x      | Verbose            | Allow comment in regex. |    
    """  
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__
    
    def __init__(self):
        self._database = None
        libraries = [
            KeePassDatabase(self),
            KeePassEntry(self),
            KeePassEntries(self),
            KeePassGroup(self),
            KeePassGroups(self)
        ]
        DynamicCore.__init__(self, libraries)

    def __enter__(self):
        return self

    def __exit__(self, typ, value, tb):
        del self._database

    def run_keyword(self, name: str, args: tuple, kwargs: dict):
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            raise

    def get_keyword_tags(self, name: str) -> list:
        tags = list(DynamicCore.get_keyword_tags(self, name))
        return tags

    def get_keyword_documentation(self, name: str) -> str:
        return DynamicCore.get_keyword_documentation(self, name)
    