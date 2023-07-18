"""Library components."""
from KeePassLibrary.base import keyword, LibraryComponent, UUID
from KeePassLibrary.errors import DatabaseNotOpened
from robot.utils import is_truthy

class KeePassEntries(LibraryComponent):
    
    # FIXME: Catch uuid string and convert to class     
    @keyword
    def get_entries(self, history=False, first=False, recursive=True,
                     path=None, group=None, **kwargs):
        """Return a list of entries in the open KeePass database matching the given arguments.\n
  
           The ``history`` argument can be set to ``True`` to include history entries in the search, default value is False.\n
           The ``first`` argument can be set ``True`` this has the effect that only the first match will be returned, default value is False.\n
           The ``recursive`` argument can be set ``True`` this enables recursive searching, default value is False.\n
           The ``path`` argument sets the path which the entries should match, default value is None.\n 
           The ``group`` argument has to match an existing Group is supplied only entries which are a direct child will be searched, default value is None. See ``Get Groups`` for information about selecting a group \n 
           See the `Entries and Groups` section for more information about Entries and Groups.\n        

           *Additional arguments:*
           - The ``regex`` argument can be set to ``True`` this enables regular expression searching, default value is False.
           - The ``flags`` argument can be set to modify the regular expression search, default value is None. See the `Regular expression` section for more information about about the ``regex`` and ``flags`` syntax.
           - The ``title`` argument can be given to search matching titles, default value is None.
           - The ``username`` argument sets the username which the entries should match, default value is None.
           - The ``password`` argument sets the password which the entries should match, default value is None.
           - The ``url`` argument sets the url which the entries should match, default value is None.
           - The ``notes`` argument sets the notes which the entries should match, default value is None.
           - The ``uuid`` argument sets the uuid which the entries should match, default value is None.
  
           Examples:
           | @{entries}= | `Get Entries` | title=.*entry | regex=True |
           | ${entry}=   | `Get Entries` | title=.*entry | regex=True | first=True |
           | @{entries}= | `Get Entries` | title=.*entry | username=.*user     | regex=True |
           | @{entries}= | `Get Entries` | title=.*entry | notes=.*entry notes | regex=True |
           
           | ${group}=   | Get Groups By Name      | subgroup | first=True |   
           | ${entries}= | Get Entries By Username | foobar   | group=${group} | first=True |     
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            if 'regex' in kwargs:
                kwargs['regex'] = is_truthy(kwargs['regex']) 
            return self.database.find_entries(recursive=recursive,
                                              path=path, 
                                              group=group,
                                              history=history, 
                                              first=first, 
                                              **kwargs)
     
    @keyword
    def get_entries_all(self):
        """Return a list of all entries in the open KeePass database.\n
           
           See the `Entries and Groups` section for more information about Entries and Groups.\n 
           
           Example:
           | ${entries} = | `Get Entries All` | 
        """
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return self.database.find_entries_by_title('.*', 
                                                       regex=True)
    
    @keyword
    def get_entries_by_title(self, title, regex=False, flags=None,
                              group=None, history=False, first=False):
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
            return self.database.find_entries_by_title(title, 
                                                       regex,
                                                       flags, 
                                                       group, 
                                                       history, 
                                                       first)
          
    @keyword
    def get_entries_by_username(self, username, regex=False, flags=None,
                                 group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database matching the given ``username``.\n
           
           See `Get Entries` for more details about optional arguments.

           Example:
           | @{entries} = | `Get Entries By Username` | foobar_user |
        """  
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return self.database.find_entries_by_username(username, 
                                                          regex, 
                                                          flags, 
                                                          group, 
                                                          history, 
                                                          first)
         
    @keyword
    def get_entries_by_password(self, password, regex=False, flags=None,
                                 group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database matching the given ``password``.\n
        
           See `Get Entries` for more details about optional arguments.
           
           Example:
           | @{entries} = | `Get Entries By Password` | passw0rd |
        """  
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return self.database.find_entries_by_password(password, 
                                                          regex, 
                                                          flags, 
                                                          group, 
                                                          history, 
                                                          first)
 
    @keyword
    def get_entries_by_url(self, url, regex=False, flags=None,
                            group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database matching the given ``url``.\n
        
           See `Get Entries` for more details about optional arguments.
           
           Example:
           | @{entries} = | `Get Entries By Url` | http://example.com |
        """  
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return self.database.find_entries_by_url(url, 
                                                     regex, 
                                                     flags, 
                                                     group, 
                                                     history, 
                                                     first)

    @keyword
    def get_entries_by_notes(self, notes, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database matching the given ``notes``.\n
        
           See `Get Entries` for more details about optional arguments.
           
           Example:
           | @{entries} = | `Get Entries By Notes` | root entry notes |
        """  
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            return self.database.find_entries_by_notes(notes,
                                         regex,
                                         flags,
                                         group,
                                         history,
                                         first)

    # FIXME: Return more then 1 match even when first is set to false
    @keyword
    def get_entries_by_path(self, entry_path_str, regex=False, flags=None,
                             group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database matching the given ``path``.\n

           See `Get Entries` for more details about optional arguments.
           
           Note, only 1 entry can be selected by path
             
           Example:
           | ${entry} = | Get Entries By Path | foobar_group/group_entry |
        """  
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            entry_path_list = entry_path_str.split('/')
            return self.database.find_entries_by_path(entry_path_list,
                                         regex,
                                         flags,
                                         group,
                                         history,
                                         first)
 
    @keyword
    def get_entries_by_uuid(self, uuid, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database matching the given ``uuid``.\n

           See `Get Entries` for more details about optional arguments.

           Example:
           | ${entries} = | Get Entries By Uuid | 12345678-1234-5678-1234-567812345678 |
        """  
        if self.database is None:
            raise DatabaseNotOpened('No KeePass Database Opened.')
        else:
            uuid = UUID('urn:uuid:'+ uuid)
            return self.database.find_entries_by_uuid(uuid,
                                         regex,
                                         flags,
                                         group,
                                         history,
                                         first)
         
    # TODO: Add documentation
    @keyword
    def get_entries_by_string(self, string, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database matching the given ``string``.\n

           See `Get Entries` for more details about optional arguments.
           
           Example:
           | &{string}= | Create Dictionary | UserName=foobar_user | Title=group_entry |  
           
           Valid dictonary keys:
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
            return self.database.find_entries_by_string(string,
                                         regex,
                                         flags,
                                         group,
                                         history,
                                         first)
            