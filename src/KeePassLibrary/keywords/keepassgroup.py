"""Library components."""
from KeePassLibrary.base import keyword, LibraryComponent, Group
from KeePassLibrary.errors import GroupInvalid
from KeePassLibrary.utils import prepare_set_timezone, convert_datetime_timezone


class KeePassGroup(LibraryComponent):

    # ---------- Base Element ----------
    @keyword
    def get_group_accessed_time(self, group: Group, timezone='UTC'):
        """Return accessed time as python
        [https://docs.python.org/library/datetime.html#datetime.datetime|datetime]
        object of the supplied KeePass ``group``.

        See the `Date and Time` section for more information about Date en Time.\n

        | =Parameter=  | =Description=                            |
        | ``group``    | A valid KeePass group                    |
        | ``timezone`` | A valid timezone string 'UTC' or 'local' |

        Example:
        | ${group} = | `Get Groups By Name`      | foobar_group | first=True   |
        | ${value} = | `Get Group Accessed Time` | ${group}     | timezone=UTC |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            value = convert_datetime_timezone(group.atime, timezone)
            return value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def set_group_accessed_time(self, group: Group, value, timezone='UTC'):
        """Sets accessed time of the supplied KeePass ``group`` to the given ``value``.

        See the `Date and Time` section for more information about Date en Time.\n

        | =Parameter=  | =Description=                            |
        | ``group``    | A valid KeePass group                    |
        | ``value``    | A valid DateTime object                  |
        | ``timezone`` | A valid timezone string 'UTC' or 'local' |

        Example:
        | ${group} =                | `Get Groups By Name` | foobar_group            | first=True |
        | ${value} =	            | Convert Date	       | 2014-06-11 10:07:42.123 | datetime   |
        | `Set Group Accessed Time` | ${entry}             | ${value}                | local      |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            value = prepare_set_timezone(value, timezone)
            group.atime = value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_created_time(self, group: Group, timezone='UTC'):
        """Return created time as python
        [https://docs.python.org/library/datetime.html#datetime.datetime|datetime]
        object of the supplied KeePass ``group``.

        See the `Date and Time` section for more information about Date en Time.\n

        | =Parameter=  | =Description=                            |
        | ``group``    | A valid KeePass group                    |
        | ``timezone`` | A valid timezone string 'UTC' or 'local' |

        Example:
        | ${group} = | `Get Groups By Name`     | foobar_group | first=True   |
        | ${value} = | `Get Group Created Time` | ${group}     | timezone=UTC |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            value = convert_datetime_timezone(group.ctime, timezone)
            return value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def set_group_created_time(self, group: Group, value, timezone='UTC'):
        """Sets created time of the supplied KeePass ``group`` to the given ``value``.

        See the `Date and Time` section for more information about Date en Time.\n

        | =Parameter=  | =Description=                            |
        | ``group``    | A valid KeePass group                    |
        | ``value``    | A valid DateTime object                  |
        | ``timezone`` | A valid timezone string 'UTC' or 'local' |

        Example:
        | ${group} =               | `Get Groups By Name` | foobar_group            | first=True |
        | ${value} =	           | Convert Date         | 2014-06-11 10:07:42.123 | datetime   |
        | `Set Group Created Time` | ${entry}             | ${value}                | local      |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            value = prepare_set_timezone(value, timezone)
            group.ctime = value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _group_delete(self, group:Group):
    #     """Not Implemented
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_expiry_time(self, group: Group, timezone='UTC'):
        """Return expiry time as python
        [https://docs.python.org/library/datetime.html#datetime.datetime|datetime]
        object of the supplied KeePass ``group``.

        See the `Date and Time` section for more information about Date en Time.\n

        | =Parameter=  | =Description=                            |
        | ``group``    | A valid KeePass group                    |
        | ``timezone`` | A valid timezone string 'UTC' or 'local' |

        Example:
        | ${group} = | `Get Groups By Name`    | foobar_group | first=True   |
        | ${value} = | `Get Group Expiry Time` | ${group}     | timezone=UTC |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            value = convert_datetime_timezone(group.expiry_time, timezone)
            return value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def set_group_expiry_time(self, group: Group, value, timezone='UTC'):
        """Sets expiry time of the supplied KeePass ``group`` to the given ``value``.

        See the `Date and Time` section for more information about Date en Time.\n

        | =Parameter=  | =Description=                            |
        | ``group``    | A valid KeePass group                    |
        | ``value``    | A valid DateTime object                  |
        | ``timezone`` | A valid timezone string 'UTC' or 'local' |

        Example:
        | ${group} =              | `Get Groups By Name` | foobar_group            | first=True |
        | ${value} =	          | Convert Date         | 2014-06-11 10:07:42.123 | datetime   |
        | `Set Group Expiry Time` | ${entry}             | ${value}                | local      |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            value = prepare_set_timezone(value, timezone)
            group.expiry_time = value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_icon(self, group: Group):
        """Return the icon of the supplied KeePass ``group``.

           Example:
           | ${group} = | `Get Groups By Name` | foobar_group | first=True |
           | ${value} = | `Get Group Icon`     | ${group}                  |

           New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.icon
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def set_group_icon(self, group: Group, value):
        """Set the ``icon`` of the supplied KeePass ``group`` to the given ``value``.

           Example:
           | ${group} = | `Get Groups By Name` | foobar_group | first=True |
           | `Set Group Expires`  | ${group}   | 20           | #Gear icon |

           New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            group.icon = value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_modified_time(self, group: Group, timezone='UTC'):
        """Return modified time as python
        [https://docs.python.org/library/datetime.html#datetime.datetime|datetime]
        object of the supplied KeePass ``group``.

        See the `Date and Time` section for more information about Date en Time.\n

        | =Parameter=  | =Description=                            |
        | ``group``    | A valid KeePass group                    |
        | ``timezone`` | A valid timezone string 'UTC' or 'local' |

        Example:
        | ${group} = | `Get Groups By Name`      | foobar_group | first=True   |
        | ${value} = | `Get Group Modified Time` | ${group}     | timezone=UTC |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            value = convert_datetime_timezone(group.mtime, timezone)
            return value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def set_group_modified_time(self, group: Group, value, timezone='UTC'):
        """Sets modified time of the supplied KeePass ``group`` to the given ``value``.

        See the `Date and Time` section for more information about Date en Time.\n

        | =Parameter=  | =Description=                            |
        | ``group``    | A valid KeePass group                    |
        | ``value``    | A valid DateTime object                  |
        | ``timezone`` | A valid timezone string 'UTC' or 'local' |

        Example:
        | ${group} =                | `Get Groups By Name` | foobar_group            | first=True |
        | ${value} =	            | Convert Date         | 2014-06-11 10:07:42.123 | datetime   |
        | `Set Group modifeid Time` | ${entry}             | ${value}                | local      |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            value = prepare_set_timezone(value, timezone)
            group.mtime = value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    # ---------- Touch ----------
    @keyword
    def touch_group(self, group: Group, modify=False):
        """Touch the supplied KeePass ``group``.

        | =Parameter= | =Description=            |
        | ``modify``  | update the modified time |

        Example:
        | ${group} =    | `Get Groups By Name` | foobar_group | first=True |
        | `Touch Group` | ${group}             | False                     |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            return group.touch(modify)
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_parent(self, group: Group):
        """Return the parentgroup of the supplied KeePass ``group``.

        Example:
        | ${group} = | `Get Groups By Name` | foobar_group | first=True |
        | ${value} = | `Get Group Parent`   | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.parentgroup
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_uuid(self, group: Group):
        """Return the uuid of the supplied KeePass ``group``.

        Example:
        | ${group} = | `Get Groups By Name` | foobar_group | first=True |
        | ${value} = | `Get Group Uuid`     | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return str(group.uuid)
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _set_group_uuid(self, group:Group, value):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_expires(self, group: Group):
        """Return expires of the supplied KeePass ``group``.

        Example:
        | ${group} = | `Get Groups By Name` | foobar_group | first=True |
        | ${value} = | `Get Group Expires`  | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.expires
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def set_group_expires(self, group: Group, value: bool):
        """Sets expires value of the supplied KeePass ``group`` to the given ``value``.

        Example:
        | ${group} =         | `Get Groups By Name` | foobar_group | first=True |
        | `Set Group Parent` | ${group}             | True                      |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            group.expires = value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_expired(self, group: Group):
        """Return expired value of the supplied KeePass ``group``.

        Example:
        | ${group} = | `Get Groups By Name` | foobar_group | first=True |
        | ${value} = | `Get Group Expired`  | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.expired
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def group_should_be_expired(self, group: Group, msg=None):
        """Fails if the specified group is not expired.

        Example:
        | ${group} =              | `Get Groups By Name` | foobar_group | first=True |
        | Set Group Expires       | ${group}             | ${TRUE}                   |
        | Group Should Be Expired | ${group}                                         |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            if not group.expired:
                message = "The group should be expired, but it is not."
                raise AssertionError(msg or message)
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def group_should_not_be_expired(self, group: Group, msg=None):
        """Fails if the specified group is expired.

        Example:
        | ${group} =                  | `Get Groups By Name` | foobar_group | first=True |
        | Set Group Expires           | ${group}             | ${FALSE}                  |
        | Group Should Not Be Expired | ${group}                                         |

        New in KeePassLibrary 0.8
        """
        if isinstance(group, Group):
            if group.expired:
                message = "The group should not be expired, but it is."
                raise AssertionError(msg or message)
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    # ---------- Group ----------
    # @keyword
    # def _group_append_entry(self, group:Group):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_entries(self, group: Group):
        """Returns a list of entries from the supplied KeePass ``group``.

        Example:
        | ${group} = | `Get Groups By Name` | foobar_group | first=True |
        | ${value} = | `Get Group Entries`  | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.entries
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_name(self, group: Group):
        """Return the name value of the supplied KeePass ``group``.

        Example:
        | ${group} = | `Get Groups By Name` | foobar_group | first=True |
        | ${value} = | `Get Group Name`     | ${group}                  |

        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.name
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def set_group_name(self, group: Group, value):
        """Set the name value of the supplied KeePass ``group`` to the given ``value``

        Example:
        | ${group} =         | `Get Groups By Name` | foobar_group | first=True |
        | `Set Group Parent` | ${group}             | new_group_name            |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            group.name = value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_notes(self, group: Group):
        """Return the notes value of the supplied KeePass ``group``.

        Example:
        | ${group} = | `Get Groups By Name` | foobar_group | first=True |
        | ${value} = | `Get Group Notes`    | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.notes
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def set_group_notes(self, group: Group, value):
        """Set the notes value of the supplied KeePass ``group`` to the given ``value``.

        Example:
        | ${group} = | `Get Groups By Name` | foobar_group | first=True |
        | ${value} = | `Get Group Notes`    | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            group.notes = value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_subgroups(self, group: Group):
        """Returns a list of subgroups from the supplied KeePass ``group``.

        Example:
        | ${group} = | `Get Groups By Name`  | foobar_group | first=True |
        | ${value} = | `Get Group Subgroups` | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.subgroups
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_is_root_group(self, group: Group):
        """Return is root group value of the supplied KeePass ``group`.`

        Example:
        | ${group} = | `Get Groups By Name`      | foobar_group | first=True |
        | ${value} = | `Get Group Is Root Group` | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.is_root_group
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def group_should_be_root_group(self, group:Group):
    #     """Verifies that the supplied ``group`` is root group.
    #
    #     """
    #     if isinstance(group, Group):
    #         return group.is_root_group
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def group_should_not_be_root_group(self, group:Group):
    #     """Verifies that the supplied ``group`` is not root group.
    #
    #     """
    #     if isinstance(group, Group):
    #         return not group.is_root_group
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_path(self, group: Group):
        """Return the path value of the supplied KeePass ``group``.

        Example:
        | ${group} = | `Get Groups By Name` | foobar_group | first=True |
        | ${value} = | `Get Group Path`     | ${group}                  |
        
        New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return "/".join(group.path)
        else:
            raise GroupInvalid('Invalid KeePass Group.')
