import os
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from .context import ContextAware
from typing import Optional


class LibraryComponent(ContextAware):
    def info(self, msg: str, html: Optional[bool] = False) -> None:
        logger.info(msg, bool(html))

    def debug(self, msg: str, html: Optional[bool] = False) -> None:
        logger.debug(msg, bool(html))

#     def log(self, msg: str, level: str = "INFO", html: bool = False):
#         if not is_noney(level):
#             logger.write(msg, level.upper(), html)

    def warn(self, msg: str, html: Optional[bool] = False) -> None:
        logger.warn(msg, bool(html))

    def log_source(self, loglevel: Optional[str] = "INFO") -> None:
        self.ctx.log_source(loglevel)

    @property
    def log_dir(self) -> str:
        try:
            logfile = BuiltIn().get_variable_value("${LOG FILE}")
            if logfile == "NONE":
                return str(BuiltIn().get_variable_value("${OUTPUTDIR}"))
            return str(os.path.dirname(logfile))
        except RobotNotRunningError:
            return str(os.getcwd())
