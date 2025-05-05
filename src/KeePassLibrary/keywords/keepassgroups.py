"""Library components."""
from KeePassLibrary.base import keyword, LibraryComponent, UUID
from KeePassLibrary.errors import DatabaseNotOpened
from robot.utils import is_truthy


class KeePassGroups(LibraryComponent):

    @keyword
    def get_groups(self, recursive=True, path=None, group=None, history=False, first=False, regex=False, flags=None, name=None, notes=None, uuid=None):
        """Return a list of groups in the open KeePass database matching the given arguments.

        The ``recursive`` argument can be set ``True`` this enables recursive searching, default value is True.\n
        The ``path`` argument sets the path which the groups should match, default value is None.\n
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
            # Create kwargs (Prevent NoneType AttributeError in find_groups)
            kwargs = {}
            if regex is not None:
                regex = is_truthy(regex)
            if first is not None:
                first = is_truthy(first)
            if uuid is not None:
                uuid = UUID('urn:uuid:' + uuid)
                kwargs['uuid'] = uuid
            return self.database.find_groups(recursive=recursive,
                                             path=path,
                                             group=group,
                                             history=history,
                                             first=first,
                                             regex=regex,
                                             flags=flags,
                                             name=name,
                                             notes=notes,
                                             **kwargs)

    @keyword
    def get_groups_all(self):
        """Return a list of all groups in the open KeePass database.

        See the `Entries and Groups` section for more information about Entries and Groups.\n

        Example:
        | ${groups} = | Get Groups All |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return self.get_groups(name='.*',
                                   regex=True)

    @keyword
    def get_groups_by_name(self, group_name, regex=False, flags=None,
                           group=None, first=False):
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
            return self.get_groups(name=group_name,
                                   regex=regex,
                                   flags=flags,
                                   group=group,
                                   first=first)

    @keyword
    def get_groups_by_path(self, group_path_str=None, regex=False, flags=None,
                           group=None, first=False):
        """Return a list of groups in the open KeePass database
        matching the given path.

        See `Get Groups` for more details about optional arguments.

        Example:
        | ${groups} = | Get Groups By Path | foobar_group/subgroup |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            group_path_list = group_path_str.split('/')
            return self.get_groups(path=group_path_list,
                                   regex=regex,
                                   flags=flags,
                                   group=group,
                                   first=first)

    @keyword
    def get_groups_by_uuid(self, uuid, regex=False, flags=None,
                           group=None, history=False, first=False):
        """Return a list of groups in the open KeePass database
        matching the given uuid.

        See `Get Groups` for more details about optional arguments.

        Example:
        | ${groups} = | Get Groups By Uuid | 12345678-1234-5678-1234-567812345678 |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return self.get_groups(uuid=uuid,
                                   regex=regex,
                                   flags=flags,
                                   group=group,
                                   history=history,
                                   first=first)

    @keyword
    def get_groups_by_notes(self, notes, regex=False, flags=None,
                            group=None, history=False, first=False):
        """Return a list of groups in the open KeePass database
        matching the given notes.

        See `Get Groups` for more details about optional arguments.

        Example:
        | ${groups} = | Get Groups By Notes | group notes |
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return self.get_groups(notes=notes,
                                   regex=regex,
                                   flags=flags,
                                   group=group,
                                   history=history,
                                   first=first)
