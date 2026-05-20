"""Library components."""
from KeePassLibrary.base import keyword, LibraryComponent, UUID, Entry, Group
from KeePassLibrary.errors import DatabaseNotOpened
from robot.utils import is_truthy
from typing import Optional, List, Dict, Union
from KeePassLibrary.utils.data_types import (
    RegExp
)

class KeePassEntries(LibraryComponent):

    # todo: path typing

    @keyword(tags=("Getter", "Entries"))
    def get_entries(self,  # type: ignore[no-untyped-def]
                    history: Optional[bool] = False,
                    first: Optional[bool] = False,
                    recursive: Optional[bool] = True,
                    path: Optional[str] = None,
                    group: Optional[Group] = None,
                    regex: Optional[bool] = False,
                    flags: Optional[str] = None,
                    title: Optional[str] = None,
                    username: Optional[str] = None,
                    password: Optional[str] = None,
                    url: Optional[str] = None,
                    notes: Optional[str] = None,
                    uuid: Optional[str] = None,
                    string: Optional[Dict[str, str]] = None) -> List[Optional[Entry]]:
        """Return a list of entries in the open KeePass database matching the given arguments.\n

        The ``history`` argument can be set to ``True`` to include history entries in the search, default value is False.\n
        The ``first`` argument can be set ``True`` this has the effect that only the first match will be returned, default value is False.\n
        The ``recursive`` argument can be set ``True`` this enables recursive searching, default value is False.\n
        The ``path`` argument sets the path which the entries should match, default value is None. This implies `first=True`. All other arguments are ignored when this is given.\n
        The ``group`` argument has to match an existing Group is supplied only entries which are a direct child will be searched, default value is None. See ``Get Groups`` for information about selecting a group \n
        See the `Entries and Groups` section for more information about Entries and Groups.\n

        *Additional arguments:*
        - The ``regex`` argument can be set to ``True`` this enables regular expression searching, default value is False.
        - The ``flags`` argument can be set to modify the regular expression search, default value is None. See the `Regular expression` section for more information about the ``regex`` and ``flags`` syntax.
        - The ``title`` argument can be given to search matching titles, default value is None.
        - The ``username`` argument sets the username which the entries should match, default value is None.
        - The ``password`` argument sets the password which the entries should match, default value is None.
        - The ``url`` argument sets the url which the entries should match, default value is None.
        - The ``notes`` argument sets the notes which the entries should match, default value is None.
        - The ``uuid`` argument sets the uuid which the entries should match, default value is None.
        - The ``string`` (dict) argument sets the custom string fields which the entries should match, default value is None.

        Examples:
        | ${entries}= | `Get Entries` | title=.*entry | regex=True |
        | ${entry}=   | `Get Entries` | title=.*entry | regex=True | first=True |
        | ${entries}= | `Get Entries` | title=.*entry | username=.*user     | regex=True |
        | ${entries}= | `Get Entries` | title=.*entry | notes=.*entry notes | regex=True |
        | ${entries}= | `Get Entries` | path=foobar_group/group_entry |

        | ${group}=   | Get Groups By Name      | subgroup | first=True |
        | ${entries}= | Get Entries By Username | foobar   | group=${group} | first=True |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            # Create kwargs (Prevent NoneType AttributeError in find_entries)
            kwargs = {}
            l_path = None
            if regex is not None:
                regex = is_truthy(regex)
            if uuid is not None:
                c_uuid = UUID('urn:uuid:' + uuid)
                kwargs['uuid'] = c_uuid
            if string is not None:
                d_string : Dict[str, str] = string
                kwargs['string'] = d_string  # type: ignore[assignment]
            if path is not None:
                l_path = str(path).split('/')
            return_entries: List[Optional[Entry]]
            return_entries = self.database.find_entries(recursive=recursive,
                                                        path=l_path,
                                                        group=group,
                                                        history=history,
                                                        first=first,
                                                        regex=regex,
                                                        flags=flags,
                                                        title=title,
                                                        username=username,
                                                        password=password,
                                                        url=url,
                                                        notes=notes,
                                                        **kwargs)
            return return_entries

    @keyword(tags=("Getter", "Entries"))
    def get_entries_all(self) -> List[Optional[Entry]]:
        """Return a list of all entries in the open KeePass database.\n

        See the `Entries and Groups` section for more information about Entries and Groups.\n

        Example:
        | ${entries} = | `Get Entries All` |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            all_entries: List[Optional[Entry]] = []
            for group in self.get_entries(recursive=True,
                                          title='.*',
                                          regex=True):
                all_entries.append(group)
            return all_entries

    @keyword(tags=("Getter", "Entries"))
    def get_entries_by_title(self,
                             title: str,
                             regex: Optional[bool] = False,
                             flags: Optional[str] = None,
                             group: Optional[Group] = None,
                             history: Optional[bool] = False,
                             first: Optional[bool] = False) -> List[Optional[Entry]]:
        """Return a list of entries in the open KeePass database matching the given ``title``.\n

        See `Get Entries` for more details about optional arguments.

        Example:
        | @{entries} = | `Get Entries By Title` | root_entry |
        => all entries with title: root_entry

        | ${entry} =   | `Get Entries By Title` | root_entry | first=True |
        => first entry with title: root_entry
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_entries = self.get_entries(title=title,
                                              regex=regex,
                                              flags=flags,
                                              group=group,
                                              history=history,
                                              first=first)
            return return_entries

    @keyword(tags=("Getter", "Entries"))
    def get_entries_by_username(self,
                                username: str,
                                regex: Optional[bool] = False,
                                flags: Union[str, RegExp, None] = None,
                                group: Optional[Group] = None,
                                history: Optional[bool] = False,
                                first: Optional[bool] = False) -> List[Optional[Entry]]:
        """Return a list of entries in the open KeePass database matching the given ``username``.\n

        See `Get Entries` for more details about optional arguments.

        Example:
        | @{entries} = | `Get Entries By Username` | foobar_user |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_entries = self.get_entries(username=username,
                                              regex=regex,
                                              flags=flags,
                                              group=group,
                                              history=history,
                                              first=first)
            return return_entries

    @keyword(tags=("Getter", "Entries"))
    def get_entries_by_password(self,
                                password: str,
                                regex: Optional[bool] = False,
                                flags: Optional[str] = None,
                                group: Optional[Group] = None,
                                history: Optional[bool] = False,
                                first: Optional[bool] = False) -> List[Optional[Entry]]:
        """Return a list of entries in the open KeePass database matching the given ``password``.\n

        See `Get Entries` for more details about optional arguments.

        Example:
        | @{entries} = | `Get Entries By Password` | passw0rd |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_entries = self.get_entries(password=password,
                                              regex=regex,
                                              flags=flags,
                                              group=group,
                                              history=history,
                                              first=first)
            return return_entries

    @keyword(tags=("Getter", "Entries"))
    def get_entries_by_url(self,
                           url: str,
                           regex: Optional[bool] = False,
                           flags: Optional[str] = None,
                           group: Optional[Group] = None,
                           history: Optional[bool] = False,
                           first: Optional[bool] = False) -> List[Optional[Entry]]:
        """Return a list of entries in the open KeePass database matching the given ``url``.\n

        See `Get Entries` for more details about optional arguments.

        Example:
        | @{entries} = | `Get Entries By Url` | https://example.com |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_entries = self.get_entries(url=url,
                                              regex=regex,
                                              flags=flags,
                                              group=group,
                                              history=history,
                                              first=first)
            return return_entries

    @keyword(tags=("Getter", "Entries"))
    def get_entries_by_notes(self,
                             notes: str,
                             regex: Optional[bool] = False,
                             flags: Optional[str] = None,
                             group: Optional[Group] = None,
                             history: Optional[bool] = False,
                             first: Optional[bool] = False) -> List[Optional[Entry]]:
        """Return a list of entries in the open KeePass database matching the given ``notes``.\n

        See `Get Entries` for more details about optional arguments.

        Example:
        | ${entries} = | `Get Entries By Notes` | root entry notes |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_entries = self.get_entries(notes=notes,
                                              regex=regex,
                                              flags=flags,
                                              group=group,
                                              history=history,
                                              first=first)
            return return_entries

    # FIXME: Return more then 1 match even when first is set to false

    @keyword(tags=("Getter", "Entries"))
    def get_entries_by_path(self,
                            path: str,
                            regex: Optional[bool] = False,
                            flags: Optional[str] = None,
                            group: Optional[Group] = None,
                            history: Optional[bool] = False,
                            first: Optional[bool] = False) -> List[Optional[Entry]]:
        """Return a list of entries in the open KeePass database matching the given ``path``.\n

        See `Get Entries` for more details about optional arguments.

        Note, only 1 entry can be selected by path

        Example:
        | ${entries} = | Get Entries By Path | foobar_group/group_entry |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_entries = self.get_entries(path=path,
                                              regex=regex,
                                              flags=flags,
                                              group=group,
                                              history=history,
                                              first=first)
            return return_entries

    @keyword(tags=("Getter", "Entries"))
    def get_entries_by_uuid(self,
                            uuid: str,
                            regex: Optional[bool] = False,
                            flags: Optional[str] = None,
                            group: Optional[Group] = None,
                            history: Optional[bool] = False,
                            first: Optional[bool] = False) -> List[Optional[Entry]]:
        """Return a list of entries in the open KeePass database matching the given ``uuid``.\n

        See `Get Entries` for more details about optional arguments.

        Example:
        | ${entries} = | Get Entries By Uuid | 12345678-1234-5678-1234-567812345678 |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_entries = self.get_entries(uuid=uuid,
                                              regex=regex,
                                              flags=flags,
                                              group=group,
                                              history=history,
                                              first=first)
            return return_entries

    @keyword(tags=("Getter", "Entries"))
    def get_entries_by_string(self,
                              string: Dict[str, str],
                              regex: Optional[bool] = False,
                              flags: Optional[str] = None,
                              group: Optional[Group] = None,
                              history: Optional[bool] = False,
                              first: Optional[bool] = False) -> List[Optional[Entry]]:
        """Return a list of entries in the open KeePass database matching the given ``string``.\n

        See `Get Entries` for more details about optional arguments.

        Example:
        | &{string} =  | Create Dictionary     | UserName=foobar_user | Title=group_entry |
        | ${entries} = | Get Entries By String | ${string}                                |

        Valid dictionary keys:
        | Title |
        | UserName |
        | Password |
        | URL |
        | Notes |
        | IconID |
        | Tags |
        | History |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_entries = self.get_entries(string=string,
                                              regex=regex,
                                              flags=flags,
                                              group=group,
                                              history=history,
                                              first=first)
            return return_entries
