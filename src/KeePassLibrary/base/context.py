from pykeepass import PyKeePass

class ContextAware:
    def __init__(self, ctx):
        """Base class exposing attributes from the common context.

        :param ctx: The library itself as a context object.
        :type ctx: keePassLibrary.keePassLibrary
        """
        self.ctx = ctx

    @property
    def database(self):
        return self.ctx._database

    @database.setter
    def database(self, value: PyKeePass):
        self.ctx._database = value
