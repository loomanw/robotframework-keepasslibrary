"""Library components."""
from KeePassLibrary.base import PyKeePass, keyword, LibraryComponent
from KeePassLibrary.errors import DatabaseNotLoaded

class KeePassDatabase(LibraryComponent):
    
    @keyword 
    def load_database(self, filename, password=None, keyfile=None,
             transformed_key=None):
        """*DEPRECATED in KeePassLibrary 0.3.0*, Use `Open Keepass Database` instead.
        """
        self.database = PyKeePass(filename,
                                  password=password,
                                  keyfile=keyfile,
                                  transformed_key=transformed_key
        )

        # capture failed to load
        self.database.read(filename, 
                           password, 
                           keyfile, 
                           transformed_key) 
    
    @keyword
    def open_keepass_database(self, filename, password=None, keyfile=None,
             transformed_key=None):
        """Opens the specified KeePass database ``filename`` using the credentials provided.
        
        The ``filename`` argument specifies the location of the KeePass database
        
        | =Parameter=        | =Description=                              |
        | ``filename``       | specifies the path of the KeePass database |
        | ``keyfile``        | specifies the path of the keyfile          |
        | ``tranformed_key`` | specifies the location of the keyfile      |
        
        Examples:
        | `Open Keepass Database` | pathtokeepassdatabase | password=mypassword   |                       |
        | `Open Keepass Database` | pathtokeepassdatabase | keyfile=pathtokeyfile |                       |
        | `Open Keepass Database` | pathtokeepassdatabase | password=mypassword   | keyfile=pathtokeyfile |
        """

        self.database = PyKeePass(filename,
                                  password=password,
                                  keyfile=keyfile,
                                  transformed_key=transformed_key
        )

        # capture failed to load
        self.database.read(filename, 
                           password, 
                           keyfile, 
                           transformed_key)

    @keyword 
    def close_database(self):
        """*DEPRECATED in KeePassLibrary 0.3.0*, Use `Close Keepass Database` instead.
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            self.database = None  
    
    @keyword    
    def close_keepass_database(self):
        """Closes the currently open KeePass database.
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            self.database = None


    
    @keyword 
    def save(self, filename=None, transformed_key=None):
        """*DEPRECATED in KeePassLibrary 0.3.0*, Use `Save Keepass Database` instead.
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            self.database.save(filename, transformed_key)        

    @keyword 
    def save_keepass_database(self, filename=None, transformed_key=None):
        """Save the content of the currently open KeePass database.

        | =Parameter=        | =Description=                              |
        | ``filename``       | specifies the path of the KeePass database |
        | ``tranformed_key`` | specifies the location of the keyfile      |
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            self.database.save(filename, transformed_key)        

    @keyword 
    def dump_xml(self, outfile):
        """Dump the content of the database to a xml file.
           NOTE: The resulting file is unencrypted!

        | =Parameter= | =Description=                        |
        | ``outfile`` | specifies the path of the dumped xml |
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            self.database.dump_xml(outfile)
    
    @keyword 
    def get_version(self):
        """Returns the version of the KeePass database loaded with `Load Database`
        | =Return=   | =Description= |
        | ``(3, 1)`` | KDBX v3       |
        | ``(4, 0)`` | KDBX v4       |
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            return self.database.version
    
    # TODO: Add more documentation
    @keyword 
    def get_encryption_algorithm(self):
        """Returns the encryption algorithm used. 
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            return self.database.encryption_algorithm
    
    # TODO: Add more documentation
    @keyword 
    def get_kdf_algorithm(self):
        """Returns the key transformation algorithm used. 
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            return self.database.kdf_algorithm
    
    # TODO: Add more documentation
    @keyword 
    def get_transformed_key(self):
        """Returns the transformed key.
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            return self.database.transformed_key

    @keyword 
    def get_tree(self):
        """Returns the full xml tree.
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            return self.database.tree

    # TODO: Add more documentation
    @keyword 
    def get_root_group(self):
        """Returns the root group.
        """
        if self.database is None:
            raise DatabaseNotLoaded('No KeePass Database loaded.')
        else:
            return self.database.root_group