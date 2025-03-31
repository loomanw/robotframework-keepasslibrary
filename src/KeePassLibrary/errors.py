class KeepassLibraryException(Exception):
    ROBOT_SUPPRESS_NAME = True


class DatabaseNotOpened(KeepassLibraryException):
    pass


class DatabaseNotFound(KeepassLibraryException):
    pass


class EntryInvalid(KeepassLibraryException):
    pass


class AttachmentInvalid(KeepassLibraryException):
    pass


class GroupInvalid(KeepassLibraryException):
    pass


class NotImplementedYet(KeepassLibraryException):
    pass


class DeprecatedKeyword(KeepassLibraryException):
    pass


class DateTimeInvalid(KeepassLibraryException):
    pass


class TimeZoneInvalid(KeepassLibraryException):
    pass
