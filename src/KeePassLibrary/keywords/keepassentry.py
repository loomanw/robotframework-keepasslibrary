"""Library components."""
from KeePassLibrary.base import keyword, LibraryComponent, Entry
from KeePassLibrary.errors import EntryInvalid


class KeePassEntry(LibraryComponent):

    # ---------- Base Element ----------

    # ---------- Title ----------
    @keyword
    def get_entry_title(self, entry: Entry):
        """Return the title value of the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True |
           | ${value} = | `Get Entry Title`      | ${entry}                |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.title
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def set_entry_title(self, entry: Entry, value):
        """Set the title value of the supplied KeePass ``entry`` to the given ``value``

           Example:
           | ${entry} =        | `Get Entries By Title` | root_entry | first=True |
           | `Set Entry Title` | New Title                                        |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.title = value
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Username ----------
    @keyword
    def get_entry_username(self, entry: Entry):
        """Return the username value of the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True |
           | ${value} = | `Get Entry Username`   | ${entry}                |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.username
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def set_entry_username(self, entry: Entry, value):
        """Set the username value of the supplied KeePass ``entry`` to the given ``value``

           Example:
           | ${entry} =           | `Get Entries By Title` | root_entry | first=True |
           | `Set Entry Username` | New Username                                     |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.username = value
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Password ----------
    @keyword
    def get_entry_password(self, entry: Entry):
        """Return the password value of the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True |
           | ${value} = | `Get Entry Password`   | ${entry}                |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.password
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def set_entry_password(self, entry: Entry, value):
        """Set the Password value of the supplied KeePass ``entry`` to the given ``value``

           Example:
           | ${entry} =           | `Get Entries By Title` | root_entry | first=True |
           | `Set Entry Password` | N3w Passw0rd                                     |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.password = value
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- URL ----------
    @keyword
    def get_entry_url(self, entry: Entry):
        """Return the URL value of the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True |
           | ${value} = | `Get Entry Url`        | ${entry}                |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.url
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def set_entry_url(self, entry: Entry, value):
        """Set the URL value of the supplied KeePass ``entry`` to the given ``value``

           Example:
           | ${entry} =      | `Get Entries By Title` | root_entry | first=True |
           | `Set Entry Url` | https://keepass.info/                            |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.url = value
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Notes ----------
    @keyword
    def get_entry_notes(self, entry: Entry):
        """Return the notes value of the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True |
           | ${value} = | `Get Entry Notes`      | ${entry}                |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.notes
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def set_entry_notes(self, entry: Entry, value):
        """Set the notes value of the supplied KeePass ``entry`` to the given ``value``

           Example:
           | ${entry} =        | `Get Entries By Title` | root_entry | first=True |
           | `Set Entry Notes` | New\\nnotes                                      |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.notes = value
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Icon ----------
    @keyword
    def get_entry_icon(self, entry: Entry):
        """Return the icon  valueof the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True |
           | ${value} = | `Get Entry Icon`       | ${entry}                |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.icon
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def set_entry_icon(self, entry: Entry, value):
        """Set the icon value of the supplied KeePass ``entry`` to the given ``value``

           Example:
           | ${entry} =        | `Get Entries By Title` | root_entry | first=True |
           | `Set Entry Icon`  | 20                                  | #Gear icon |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.icon = value
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Tags (not implemented) ----------
    @keyword
    def get_entry_tags(self, entry: Entry):
        """Return a list with tags of the supplied KeePass ``entry``

            Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True |
           | ${value} = | `Get Entry Tags`       | ${entry}                |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.tags
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def set_entry_tags(self, entry: Entry, value):
        """Set the tags value of the supplied KeePass ``entry`` to the given ``value``

           Example:
           | @{tags}=       | Create List | tag1     | tag2 |
           | Set Entry Tags | ${entry}   | ${tags}   | |
           | Set Entry Tags | ${entry}   | tag1;tag2 | |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.tags = value
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- History (not fully implemented) ----------
    # FIXME: not implented
    # @property
    # def history(self):
    #     if self._element.find('History') is not None:
    #         return [Entry(element=x, kp=self._kp) for x in self._element.find('History').findall('Entry')]
    #     else:
    #         return []

    # FIXME: not implented
    # @history.setter
    # def history(self, value):
    #     raise NotImplementedError()

    # def save_history(self):
    #     '''
    #     Save the entry in its history
    #     '''
    #     archive = deepcopy(self._element)
    #     hist = archive.find('History')
    #     if hist is not None:
    #         archive.remove(hist)
    #         self._element.find('History').append(archive)
    #     else:
    #         history = Element('History')
    #         history.append(archive)
    #         self._element.append(history)

    # @keyword
    # def entry_should_be_history_entry(self, entry:Entry):
    #     """Verifies that the specified entry is history entry.
    #
    #        Example:
    #        | ${entry} = | `Get Entries By Title` | root_entry | first=True |
    #        | `Entry Should Be History Entry`     | ${entry}                |
    #
    #        New in KeePassLibrary 0.3
    #     """
    #     if isinstance(entry, Entry):
    #         if not entry.is_a_history_entry:
    #             raise EntryInvalid('Entry is not a history entry.')
    #     else:
    #         raise EntryInvalid('Invalid KeePass Entry.')

    # #@keyword
    # def entry_should_not_be_history_entry(self, entry:Entry):
    #     """Verifies that the specified entry is history entry.
    #
    #        Example:
    #        | ${entry} = | `Get Entries By Title` | root_entry | first=True |
    #        | `Entry Should Not Be History Entry` | ${entry}                |
    #
    #        New in KeePassLibrary 0.3
    #     """
    #     if isinstance(entry, Entry):
    #         if entry.is_a_history_entry:
    #             raise EntryInvalid('Entry is a history entry.')
    #     else:
    #         raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Autotype (not implemented)----------
    # @property
    # def autotype_enabled(self):
    #     enabled = self._element.find('AutoType/Enabled')
    #     if enabled.text is not None:
    #         return enabled.text == 'True'

    # @autotype_enabled.setter
    # def autotype_enabled(self, value):
    #     enabled = self._element.find('AutoType/Enabled')
    #     if value is not None:
    #         enabled.text = str(value)
    #     else:
    #         enabled.text = None

    # ---------- Autotype sequence (not implemented)----------
    # @property
    # def autotype_sequence(self):
    #     sequence = self._element.find('AutoType/DefaultSequence')
    #     return sequence.text if sequence is not None else None

    # @autotype_sequence.setter
    # def autotype_sequence(self, value):
    #     self._element.find('AutoType/DefaultSequence').text = value

    # @property
    # def path(self):
    #     # The root group is an orphan
    #     if self.is_a_history_entry:
    #         pentry = Entry(
    #             element=self._element.getparent().getparent(),
    #             kp=self._kp
    #         ).title
    #         return '[History of: {}]'.format(pentry)
    #     if self.parentgroup is None:
    #         return None
    #     p = self.parentgroup
    #     ppath = ''
    #     while p is not None and not p.is_root_group:
    #         if p.name is not None:  # dont make the root group appear
    #             ppath = '{}/{}'.format(p.name, ppath)
    #         p = p.parentgroup
    #     return '{}{}'.format(ppath, self.title)

    # ---------- Custom Property ----------

    @keyword
    def set_entry_custom_property(self, entry: Entry, key, value):
        """Sets property ``key`` of the supplied ``entry`` to ``value``.

           Example:
           | ${entry} =                  | `Get Entries By Title` | root_entry | first=True |
           | `Set Entry Custom Property` | new_field_name         | new_field_value         |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.set_custom_property(key, value)
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def get_entry_custom_property(self, entry: Entry, key):
        """Return the value from a custom property matching the given ``key`` of the supplied ``entry``

           Example:
           | ${entry} = | `Get Entries By Title`      | root_entry | first=True       |
           | ${value} = | `Get Entry Custom Property` | ${entry}   | foobar_attribute |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.get_custom_property(key)
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def remove_entry_custom_property(self, entry: Entry, key):
        """Removes a custom property matching the given key of the supplied KeePass ``entry``

           Example:
           | ${entry} =                     | `Get Entries By Title`      | root_entry | first=True       |
           | `Remove Entry Custom Property` | ${entry}                    | foobar_attribute              |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.delete_custom_property(key)
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def get_entry_custom_properties(self, entry: Entry):
        """Return a dictonary with all custom properties of the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title`        | root_entry | first=True       |
           | ${value} = | `Get Entry Custom Properties` | ${entry}                      |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.custom_properties
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Reference (not implemented) ----------
    # def deref(self, attribute):
    #     return self._kp.deref(getattr(self, attribute))

    # def ref(self, attribute):
    #     """Create reference to an attribute of this element."""
    #     attribute_to_field = {
    #         'title': 'T',
    #         'username': 'U',
    #         'password': 'P',
    #         'url': 'A',
    #         'notes': 'N',
    #         'uuid': 'I',
    #     }
    #     return '{{REF:{}@I:{}}}'.format(attribute_to_field[attribute], self.uuid.hex.upper())
    # ---------- (parent)Group ----------

    # ---------- Dump XML (not implemented) ----------
    # @keyword
    # def get_entry_xml(self, entry:Entry, pretty_print=False):
    #     """Return the XML of the supplied KeePass ``entry``
    #     """
    #     if isinstance(entry, Entry):
    #         entry.dump_xml(pretty_print)
    #     else:
    #         raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- UUID ----------
    @keyword
    def get_entry_uuid(self, entry: Entry):
        """Return the UUID value of the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True       |
           | ${value} = | `Get Entry Uuid`       | ${entry}                      |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return str(entry.uuid)
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # @keyword
    # def set_entry_uuid(self, entry:Entry, value):
    #     """Set the ``UUID`` of the supplied KeePass ``entry`` to the given ``value``
    #     """
    #     if isinstance(entry, Entry):
    #         entry.uuid = value
    #     else:
    #         raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Expired ----------
    @keyword
    def get_entry_expired(self, entry: Entry):
        """Return expired value of the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True       |
           | ${value} = | `Get Entry Expired`    | ${entry}                      |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.expired
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # @keyword
    # def entry_should_be_expired(self, entry:Entry, message=None):
    #     """Fails if the specified entry is not expired.
    #
    #        Example:
    #        | ${entry} = | `Get Entries By Title` | root_entry | first=True       |
    #        | ${value} = | `Get Entry Expired`    | ${entry}                      |
    #
    #        New in KeePassLibrary 0.3
    #     """
    #     if isinstance(entry, Entry):
    #         if is_noney(message):
    #             message = f"The element '{entrylocator}' should be visible, but it is not."
    #         raise AssertionError(message)
    #     else:
    #         raise EntryInvalid('Invalid KeePass Entry.')

    # @keyword
    # def entry_should_not_be_expired(self, entry:Entry):
    #     """Verifies that the specified entry is not expired.
    #
    #        New in KeePassLibrary 0.3
    #     """
    #     if isinstance(entry, Entry):
    #         return not entry.expired
    #     else:
    #         raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Expires ----------
    @keyword
    def set_entry_expires(self, entry: Entry, value: bool):
        """Sets expires value of the supplied KeePass ``entry`` to the given ``value``.

           Example:
           | ${entry} =          | `Get Entries By Title` | root_entry | first=True |
           | `Set Entry Expires` | ${entry}               | True                    |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            entry.expires = value
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    @keyword
    def get_entry_expires(self, entry: Entry):
        """Return expires value of the supplied KeePass ``entry``

           Example:
           | ${entry} = | `Get Entries By Title` | root_entry | first=True       |
           | ${value} = | `Get Entry Expires`    | ${entry}                      |

           New in KeePassLibrary 0.3
        """
        if isinstance(entry, Entry):
            return entry.expires
        else:
            raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Expired Time ----------
    # FIXME: not implented
    # @keyword
    # def get_entry_expiry_time(self, entry:Entry):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # FIXME: not implented
    # @keyword
    # def set_entry_expiry_time(self, entry:Entry, value):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # ---------- Created Time ----------
    # FIXME: not implented
    # @keyword
    # def get_entry_created_time(self, entry:Entry):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # FIXME: not implented
    # @keyword
    # def set_entry_created_time(self, entry:Entry, value):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # ---------- Last Access Time ----------
    # FIXME: not implented
    # @keyword
    # def get_entry_last_access_time(self, entry:Entry):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # FIXME: not implented
    # @keyword
    # def set_entry_last_access_time(self, entry:Entry, value):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # ---------- Modified Time ----------
    # FIXME: not implented
    # @keyword
    # def get_entry_modified_time(self, entry:Entry):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # FIXME: not implented
    # @keyword
    # def set_entry_modified_time(self, entry:Entry, value):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # ---------- Touch ----------
    # @keyword
    # def entry_touch(self, entry:Entry, modify=False):
    #     """Update last access time of an entry
    #     """
    #     if isinstance(entry, Entry):
    #         return entry.touch(modify)
    #     else:
    #         raise EntryInvalid('Invalid KeePass Entry.')

    # ---------- Attachements (not implemented) ----------
    # TODO: Implented
    # @keyword
    # def get_entry_attachments(self, entry:Entry):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # def attachments(self):
    #     return self._kp.find_attachments(
    #         element=self,
    #         filename='.*',
    #         regex=True,
    #         recursive=False
    #     )

    # TODO: Implented
    # @keyword
    # def add_entry_attachment(self, entry:Entry, ide):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # def add_attachment(self, id, filename):
    #     element = E.Binary(
    #         E.Key(filename),
    #         E.Value(Ref=str(id))
    #     )
    #     self._element.append(element)
    #     return pykeepass.attachment.Attachment(element=element, kp=self._kp)

    # TODO: Implented
    # @keyword
    # def remove_entry_attachment(self, entry:Entry, ide):
    #     """*DEPRECATED*
    #     """
    #     raise NotImplementedYet('this keyword is not implemented.')

    # def delete_attachment(self, attachment):
    #     attachment.delete()
