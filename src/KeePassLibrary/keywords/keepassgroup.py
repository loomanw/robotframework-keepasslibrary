"""Library components."""
from KeePassLibrary.base import keyword, LibraryComponent, Group
from KeePassLibrary.errors import GroupInvalid


class KeePassGroup(LibraryComponent):

    # ---------- Base Element ----------
    # @keyword
    # def _get_group_accessed_time(self, group:Group):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _set_group_accessed_time(self, group:Group, value):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _get_group_created_time(self, group:Group):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _set_group_created_time(self, group:Group, value):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _group_delete(self, group:Group):
    #     """Not Implemented
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _get_group_expiry_time(self, group:Group):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _set_group_expiry_time(self, group:Group, value):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_icon(self, group: Group):
        """Return the icon of the supplied KeePass ``group``

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
        """Set the ``icon`` of the supplied KeePass ``group`` to the given ``value``

           Example:
           | ${group} = | `Get Groups By Name` | foobar_group | first=True |
           | `Set Group Expires`  | ${group}   | 20           | #Gear icon |

           New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            group.icon = value
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _get_group_modified_time(self, group:Group):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def _set_group_modified_time(self, group:Group, value):
    #     """*DEPRECATED*
    #     """
    #     if isinstance(group, Group):
    #         raise NotImplementedYet('This keyword is not implemented.')
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_parent(self, group: Group):
        """Return the parentgroup of the supplied KeePass ``group``

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
        """Return the uuid of the supplied KeePass ``group``

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
        """Return expires of the supplied KeePass ``group``

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
        """Sets expires value of the supplied KeePass ``group`` to the given ``value``

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
        """Return expired value of the supplied KeePass ``group``

           Example:
           | ${group} = | `Get Groups By Name` | foobar_group | first=True |
           | ${value} = | `Get Group Expired`  | ${group}                  |

           New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return group.expired
        else:
            raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def group_should_be_expired(self, group:Group):
    #     """Verifies that the supplied ``group`` is expired
    #
    #        New in KeePassLibrary 0.3
    #     """
    #     if isinstance(group, Group):
    #         return group.expired
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def group_should_not_be_expired(self, group:Group):
    #     """Verifies that the supplied ``group`` is not expired
    #     """
    #     if isinstance(group, Group):
    #         return not group.expired
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

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
        """Returns a list of entries from the supplied KeePass ``group``

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
        """Return the name value of the supplied KeePass ``group``

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
        """Return the notes value of the supplied KeePass ``group``

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
        """Set the notes value of the supplied KeePass ``group`` to the given ``value``

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
        """Returns a list of subgroups from the supplied KeePass ``group``

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
        """Return is root group value of the supplied KeePass ``group``

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
    #        New in KeePassLibrary 0.3
    #     """
    #     if isinstance(group, Group):
    #         return group.is_root_group
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    # @keyword
    # def group_should_not_be_root_group(self, group:Group):
    #     """Verifies that the supplied ``group`` is not root group.
    #
    #        New in KeePassLibrary 0.3
    #     """
    #     if isinstance(group, Group):
    #         return not group.is_root_group
    #     else:
    #         raise GroupInvalid('Invalid KeePass Group.')

    @keyword
    def get_group_path(self, group: Group):

        """Return the path value of the supplied KeePass ``group``

           Example:
           | ${group} = | `Get Groups By Name` | foobar_group | first=True |
           | ${value} = | `Get Group Path`     | ${group}                  |

           New in KeePassLibrary 0.3
        """
        if isinstance(group, Group):
            return "/".join(group.path)
        else:
            raise GroupInvalid('Invalid KeePass Group.')
