import subprocess
import sys

from pykeepass import __version__ as pk__version__
from KeePassLibrary import __version__ as kpl__version__


def get_rf_version() -> str:
    process = subprocess.run(
        [sys.executable, "-m", "robot", "--version"], capture_output=True, check=False
    )
    return process.stdout.decode("utf-8").split(" ")[2]


def get_version():
    """Display Python, Robot Framework, KeePassLibrary and PyKeePass versions"""
    python_version = (
        f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )
    return (
        f"\nUsed Python is: {sys.executable}\n\tVersion: {python_version}\n"
        f'Robot Framework version: "{get_rf_version()}"\n'
        f"Installed KeePassLibrary version is: {kpl__version__}\n"
        f"Installed PyKeePass version is: {pk__version__}\n"
    )
