from pykeepass import PyKeePass
# from pykeepass import entry
# from pykeepass import group

__version__ = '0.2.5'

class KeePassLibrary(object):

    """KeepassLibrary is a library for Robot Framework.
    
    KeepassLibrary uses the PyKeePass modules internally to
    access KeePass databases
    
    See https://keepass.info for more information about KeePass in general.
    
    == Entry ==
    
    A returned entry may have one of the following attributes, attributes that contain no data are not accessible.
    
    | = Attribute = | = Example = |
    | title | ${entry.title} |
    | username | ${entry.username} |
    | password | ${entry.password} |
    | url | ${entry.url} |
    | tags | ${entry.tags} |
    | icon | ${entry.icon} |  
    
    == Groups ==
    
    A returned group may have one of the following attributes, attributes that contain no data are not accessible.
    | = Attribute = | = Example = |
    | name | ${group.name} |
    | notes | ${group.notes} |
    | entries | ${group.entries} |
    | subgroups | ${group.subgroups} |
    | is_root_group | ${group.is_root_group} |    
    | path | ${group.path} |

    """   
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__
    
    def __init__(self):
        self._kp = None
    
    def __enter__(self):
        return self

    def __exit__(self, typ, value, tb):
        del self._kp
    #---------- Database ----------
    # TODO: Update documentation
    def load_database(self, filename, password=None, keyfile=None,
             transformed_key=None):
        """Loads the specified KeePass database ``filename`` using the credentials provided.
        
        The ``filename`` argument specifies the location of the KeePass database
        
        | =Parameter=        | =Description=                              |
        | ``filename``       | specifies the path of the KaaPass database |
        | ``keyfile``        | specifies the path of the keyfile          |
        | ``tranformed_key`` | specifies the location of the keyfile      |
        
        Examples:
        | `Load Database` | pathtokeepassdatabase | password= mypassword  |                       |
        | `Load Database` | pathtokeepassdatabase | keyfile=pathtokeyfile |                       |
        | `Load Database` | pathtokeepassdatabase | password=mypassword   | keyfile=pathtokeyfile |
        """

        # TODO: capture failed to load
        self._kp = PyKeePass(filename,
                             password=password,
                             keyfile=keyfile,
                             transformed_key=transformed_key
        )

        # TODO: capture failed to load
        self._kp = PyKeePass(filename,
                             password=password,
                             keyfile=keyfile,
                             transformed_key=transformed_key)
        
    # TODO: Add more documentation
    def close_database(self):
        """Closes the currently open database.
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            self._kp = None
    
    # TODO: Add more documentation
    def save(self, filename=None, transformed_key=None):
        """Save the content of the currently open database.
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            self._kp.save(filename, transformed_key)        

    # TODO: Add more documentation
    def dump_xml(self, outfile):
        """Save the content of the database to a xml file.
           NOTE: The resulting file is unencrypted!
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            self._kp.dump_xml(outfile)
    
    # TODO: Add more documentation
    def get_version(self):
        """Returns the version of the KeePass database loaded with `Load Database`
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.version
    
    # TODO: Add more documentation
    def get_encryption_algorithm(self):
        """Returns the encryption algorithm used. 
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.encryption_algorithm
    
    # TODO: Add more documentation
    def get_kdf_algorithm(self):
        """Returns the key transformation algorithm used. 
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.kdf_algorithm
    
    # TODO: Add more documentation
    def get_transformed_key(self):
        """Returns the transformed key.
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.transformed_key

    # TODO: Add more documentation
    def get_tree(self):
        """Returns the full tree
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.tree

    # TODO: Add more documentation
    def get_root_group(self):
        """Returns the root group
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.root_group

    #---------- Entries ----------
    # todo: add get entry attribute
    
    
    # TODO: Add documentation
    def get_entries(self, history=False, first=False, recursive=True,
                     path=None, group=None, **kwargs):
        """Return a list of all entries in the open KeePass database
        matching the given options
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries(history, 
                                         first, 
                                         recursive, 
                                         path, 
                                         group, 
                                         **kwargs)
        
    # TODO: Add documentation
    def get_entries_all(self):
        """Return a list of all entries in the open KeePass database
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries_by_title('.*', regex=True)
    
    # TODO: Add documentation
    def get_entries_by_title(self, title, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
        matching the given title
        """        
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries_by_title(title, 
                                                  regex,
                                                  flags, 
                                                  group, 
                                                  history, 
                                                  first)
          
    # TODO: Add documentation
    def get_entries_by_username(self, username, regex=False, flags=None,
                                 group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
        matching the given username
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries_by_username(username, 
                                                     regex, 
                                                     flags, 
                                                     group, 
                                                     history, 
                                                     first)
         
    # TODO: Add documentation
    def get_entries_by_password(self, password, regex=False, flags=None,
                                 group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
           matching the given password
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries_by_password(password, 
                                                     regex, 
                                                     flags, 
                                                     group, 
                                                     history, 
                                                     first)
 
    # TODO: Add documentation
    def get_entries_by_url(self, url, regex=False, flags=None,
                            group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
           matching the given url
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries(url, 
                                         regex, 
                                         flags, 
                                         group, 
                                         history, 
                                         first)

    # TODO: Add documentation
    def get_entries_by_notes(self, notes, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
           matching the given notes
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries(notes,
                                         regex,
                                         flags,
                                         group,
                                         history,
                                         first)

    # TODO: Add documentation
    def get_entries_by_path(self, path, regex=False, flags=None,
                             group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
           matching the given path
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries(path,
                                         regex,
                                         flags,
                                         group,
                                         history,
                                         first)
 
    # TODO: Add documentation
    def get_entries_by_uuid(self, uuid, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
           matching the given uuid
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries(uuid,
                                         regex,
                                         flags,
                                         group,
                                         history,
                                         first)
         
    # TODO: Add documentation
    def get_entries_by_string(self, string, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
           matching the given string  
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries(string,
                                         regex,
                                         flags,
                                         group,
                                         history,
                                         first)
            
    #---------- Groups ---------- 
    # TODO: Add more documentation
    def get_groups(self, recursive=True, path=None, group=None, **kwargs):
        """Return a list of groups in the open KeePass database
           matching the given string
        """ 
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_groups(recursive, path, group, **kwargs)
    
    # TODO: Add more documentation
    def get_groups_all(self):
        """Return a list of all groups in the open KeePass database.
        """ 
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_groups_by_name('.*', regex=True)
        
    # TODO: Add more documentation
    def get_groups_by_name(self, group_name, regex=False, flags=None,
                            group=None, first=False):
        """Return a list of groups in the open KeePass database
           matching the given string
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self.get_groups(name=group_name,
                                        regex=regex,
                                        flags=flags,
                                        group=group,
                                        first=first)
    
    # TODO: Add more documentation
    def get_groups_by_path(self, group_path_str=None, regex=False, flags=None,
                            group=None, first=False):
        """Return a list of groups in the open KeePass database
           matching the given path
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self.get_groups(path=group_path_str,
                                   regex=regex,
                                   flags=flags,
                                   group=group,
                                   first=first)
 
    # TODO: Add more documentation
    def get_groups_by_uuid(self, uuid, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of groups in the open KeePass database
           matching the given uuid
        """ 
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self.get_groups(uuid=uuid,
                                   regex=regex,
                                   flags=flags,
                                   group=group,
                                   history=history,
                                   first=first)

    # TODO: Add more documentation
    def get_groups_by_notes(self, notes, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of groups in the open KeePass database
           matching the given notes
        """ 
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self.get_groups(notes=notes,
                                   regex=regex,
                                   flags=flags,
                                   group=group,
                                   history=history,
                                   first=first)
  
class KeepassLibraryError(Exception):
    pass  
    