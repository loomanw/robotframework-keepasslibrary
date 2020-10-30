import os
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from .context import ContextAware

class LibraryComponent(ContextAware):
    def info(self, msg: str, html: bool = False):
        logger.info(msg, html)

    def debug(self, msg, html=False):
        logger.debug(msg, html)

#     def log(self, msg: str, level: str = "INFO", html: bool = False):
#         if not is_noney(level):
#             logger.write(msg, level.upper(), html)

    def warn(self, msg: str, html: bool = False):
        logger.warn(msg, html)

    def log_source(self, loglevel: str = "INFO"):
        self.ctx.log_source(loglevel)

    @property
    def log_dir(self):
        try:
            logfile = BuiltIn().get_variable_value("${LOG FILE}")
            if logfile == "NONE":
                return BuiltIn().get_variable_value("${OUTPUTDIR}")
            return os.path.dirname(logfile)
        except RobotNotRunningError:
            return os.getcwd()
