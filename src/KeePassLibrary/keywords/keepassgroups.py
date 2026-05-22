"""Library components."""
# from mypy.stubgen import EMPTY

from KeePassLibrary.base import keyword, LibraryComponent, UUID, Group
from KeePassLibrary.errors import DatabaseNotOpened
from typing import Optional, List, Dict


class KeePassGroups(LibraryComponent):

    @keyword(tags=("Getter", "Groups"))
    def get_groups(self, recursive: Optional[bool] = False,
                   path: Optional[str] = None,
                   group: Optional[Group] = None,
                   uuid: Optional[str] = None,
                   name: Optional[str] = None,
                   notes: Optional[str] = None,
                   history: Optional[bool] = False,
                   first: Optional[bool] = False,
                   regex: Optional[bool] = False,
                   flags: Optional[str] = None) -> List[Group]:
        """Return a list of groups in the open KeePass database matching the given arguments.

        The ``recursive`` argument can be set ``True`` this enables recursive searching, default value is False.\n
        The ``path`` argument sets the path which the groups should match, default value is None. This implies `first=True`. All other arguments are ignored when this is given.\n
        The ``group`` argument has to match an existing Group is supplied only entries which are a direct child will be searched, default value is None. See ``Get Groups`` for information about selecting a group \n
        See the `Entries and Groups` section for more information about Entries and Groups.\n

        *Additional arguments:*
        - The ``history`` argument can be set to ``True`` to include history groups in the search, default value is False.
        - The ``first`` argument can be set ``True`` this has the effect that only the first match will be returned, default value is False.
        - The ``regex`` argument can be set to ``True`` this enables regular expression searching, default value is False.
        - The ``flags`` argument can be set to modify the regular expression search, default value is None. See the `Regular expression` section for more information about the ``regex`` and ``flags`` syntax.
        - The ``name`` argument can be given to search matching names, default value is None.
        - The ``notes`` argument sets the notes which the groups should match, default value is None.
        - The ``uuid`` argument sets the uuid which the groups should match, default value is None.

        Example:
        | @{groups}= | `Get Groups` | name=.*group | notes=^.{0}$ | regex=True              |
        | ${groups}= | `Get Groups` | name=.*group | notes=^.{0}$ | regex=True | first=True |

        | ${group}=   | `Get Groups By Name` | subgroup  | first=True     |
        | @{groups}= |  `Get Groups`         | subgroup2 | group=${group} |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_groups: List[Group] = []
            l_path = None
            kwargs: Dict[str, UUID] = {}
            if uuid is not None:
                kwargs.update({'uuid': UUID('urn:uuid:' + uuid)})
            if path is not None:
                l_path = str(path).split('/')
            found_groups = self.database.find_groups(recursive=bool(recursive),
                                                     path=l_path,
                                                     group=group,
                                                     history=history,
                                                     first=first,
                                                     regex=regex,
                                                     flags=flags,
                                                     name=name,
                                                     notes=notes,
                                                     **kwargs)
            if isinstance(found_groups, list):
                for item in found_groups:
                    if isinstance(item, Group):
                        return_groups.append(item)
            else:
                if isinstance(found_groups, Group):
                    return_groups.append(found_groups)
            return return_groups

    @keyword(tags=("Getter", "Groups"))
    def get_groups_all(self) -> List[Optional[Group]]:
        """Return a list of all groups in the open KeePass database.

        See the `Entries and Groups` section for more information about Entries and Groups.\n

        Example:
        | ${groups} = | Get Groups All |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            all_groups: List[Optional[Group]] = []
            for group in self.get_groups(recursive=True,
                                         name='.*',
                                         regex=True):
                all_groups.append(group)
            return all_groups

    @keyword(tags=("Getter", "Groups"))
    def get_groups_by_name(self, name: str, regex: Optional[bool] = False, flags: Optional[str] = None,
                           group: Optional[Group] = None, first: Optional[bool] = False) -> List[Group]:
        """Return a list of groups in the open KeePass database
        matching the given string.

        See `Get Groups` for more details about optional arguments.

        Examples:
        | ${groups} = | Get Groups By Name | subgroup              |
        | ${groups} = | Get Groups By Name | .*       | regex=True |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_groups: List[Group] = []
            return_groups = self.get_groups(recursive=True,
                                            name=name,
                                            regex=regex,
                                            flags=flags,
                                            group=group,
                                            first=first)
            return return_groups

    @keyword(tags=("Getter", "Groups"))
    def get_groups_by_path(self, path: str, regex: Optional[bool] = False, flags: Optional[str] = None,
                           group: Optional[Group] = None, first: Optional[bool] = False) -> List[Group]:
        """Return a list of groups in the open KeePass database
        matching the given path.

        See `Get Groups` for more details about optional arguments.

        Example:
        | ${groups} = | Get Groups By Path | foobar_group/subgroup |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_groups: List[Group] = []
            return_groups = self.get_groups(recursive=True,
                                            path=path,
                                            regex=regex,
                                            flags=flags,
                                            group=group,
                                            first=first)
            return return_groups

    @keyword(tags=("Getter", "Groups"))
    def get_groups_by_uuid(self, uuid: str, regex: Optional[bool] = False, flags: Optional[str] = None,
                           group: Optional[Group] = None, history: Optional[bool] = False, first: Optional[bool] = False) -> List[Group]:
        """Return a list of groups in the open KeePass database
        matching the given uuid.

        See `Get Groups` for more details about optional arguments.

        Example:
        | ${groups} = | Get Groups By Uuid | 12345678-1234-5678-1234-567812345678 |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_groups: List[Group] = []
            return_groups = self.get_groups(recursive=True,
                                            uuid=uuid,
                                            regex=regex,
                                            flags=flags,
                                            group=group,
                                            history=history,
                                            first=first)
            return return_groups

    @keyword(tags=("Getter", "Groups"))
    def get_groups_by_notes(self, notes: str, regex: Optional[bool] = False, flags: Optional[str] = None,
                            group: Optional[Group] = None, history: Optional[bool] = False, first: Optional[bool] = False) -> List[Group]:
        """Return a list of groups in the open KeePass database
        matching the given notes.

        See `Get Groups` for more details about optional arguments.

        Example:
        | ${groups} = | Get Groups By Notes | group notes |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return_groups: List[Group] = []
            return_groups = self.get_groups(recursive=True,
                                            notes=notes,
                                            regex=regex,
                                            flags=flags,
                                            group=group,
                                            history=history,
                                            first=first)
            return return_groups
