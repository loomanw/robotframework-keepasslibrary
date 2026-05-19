from pykeepass import PyKeePass
from typing import Union


class ContextAware:
    def __init__(self, ctx) -> None:  # type: ignore[no-untyped-def]
        """Base class exposing attributes from the common context.

        :param ctx: The library itself as a context object.
        :type ctx: keePassLibrary.keePassLibrary
        """
        self.ctx = ctx

    @property
    def database(self) -> Union[PyKeePass, None]:
        db: PyKeePass = self.ctx.database
        return db

    @database.setter
    def database(self, value: Union[PyKeePass, None]) -> None:
        self.ctx.database = value
