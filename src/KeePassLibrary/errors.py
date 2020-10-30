class KeepassLibraryException(Exception):
    ROBOT_SUPPRESS_NAME = True
 
class DatabaseNotLoaded(KeepassLibraryException):
    pass
 
class DatabaseNotFound(KeepassLibraryException):
    pass

class EntryInvalid(KeepassLibraryException):
    pass

class GroupInvalid(KeepassLibraryException):
    pass

class NotImplementedYet(KeepassLibraryException):
    pass

class DeprecatedKeyword(KeepassLibraryException):
    pass
