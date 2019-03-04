from pykeepass import PyKeePass

__version__ = '0.1.0'

class KeePassLibrary(object):

    """KeepassLibrary is a library for Robot Framework.
    
    KeepassLibrary uses the PyKeePass modules internally to
    access KeePass databases
    
    See https://keepass.info for more information about KeePass in general.
    
    == Entry ==
    
    A returned entry may have one of the following attributes, attributes that contain no data are not accessible.
    
    | = Attribute = | = Example = |
    | Title | ${entry.title} |
    | UserName | ${entry.usernam} |
    | Password | ${entry.password} |
    | url | ${entry.url} |
    | tags | ${entry.tags} |
    | iconid | ${entry.icondid} |
    | times | ${entry.times} |
    | history | ${entry.history} |
    
    
    == Groups ==
    
    Group are not impemented yet.
    
    """   
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__
        
    def __init__(self):
        self._kp = None
    
    def __enter__(self):
        return self

    def __exit__(self, typ, value, tb):
        del self._kp
    
    # TODO: Update documentation
    def load_database(self, filename, password=None, keyfile=None,
             transformed_key=None):
        """Loads the specified KeePass database ``filename`` using the credentials provided.
        
        The ``filename`` argument specifies the location of the KeePass database
        
        Optional ``password`` is 
        Optional ``keyfile`` specifies the location of the keyfile
        Optional ``keyfile`` specifies the location of the keyfile
        
        Examples:
        | Load Database | ``filename`` | password= ``password``                       |
        | Load Database | ``filename`` | keyfile= ``keyfile``                         |
        | Load Database | ``filename`` | password= ``password``  keyfile= ``keyfile`` |
        """

        # TODO: capture failed to load
        self._kp = PyKeePass(
            filename,
            password=password,
            keyfile=keyfile,
            transformed_key=transformed_key
        )

    # TODO: Add more documentation
    def close_database(self):
        """Closes the currently open database.
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            self._kp = None
            
    # TODO: Add more documentation
    def dump_xml(self, outfile):
        """Save the content of the database to a xml file.
           NOTE: The resulting file is unencrypted!
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            self._kp.dump_xml(outfile)
            
    #---------- Getters -------
    # TODO: Add more documentation
    def get_version(self):
        """Returns the version of the KeePass database loaded with `Load Database`
        """
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.version
    
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
                                                 first
                                                 )
 
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
                                     first
        )

    # TODO: Add documentation
    def get_entries_by_path(self, path, regex=False, flags=None,
                             group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
           matching the given path
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries(
                                     path,
                                     regex,
                                     flags,
                                     group,
                                     history,
                                     first
        )
 
    # TODO: Add documentation
    def get_entries_by_uuid(self, uuid, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
           matching the given uuid
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries(
                                    uuid,
                                    regex,
                                    flags,
                                    group,
                                    history,
                                    first
        )
         
    # TODO: Add documentation
    def get_entries_by_string(self, string, regex=False, flags=None,
                              group=None, history=False, first=False):
        """Return a list of entries in the open KeePass database
           matching the given string
        """  
        if self._kp is None:
            raise KeepassLibraryError('No KeePass Database loaded.')
        else:
            return self._kp.find_entries(
                                    string,
                                    regex,
                                    flags,
                                    group,
                                    history,
                                    first
        )
          
class KeepassLibraryError(Exception):
    pass  
    
    
