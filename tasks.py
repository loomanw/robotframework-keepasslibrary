# import sys
from pathlib import Path

from invoke import task
from rellu import Version
from rellu.tasks import clean  # noqa
from robot.libdoc import libdoc

assert Path.cwd() == Path(__file__).parent

VERSION_PATTERN = '__version__ = "(.*)"'
VERSION_PATH = Path("src/KeePassLibrary/__init__.py")


@task
def kw_docs(ctx, version=None):
    """Generates the library keyword documentation.
    Args:
        version:  Appends version to the end of the filename.
                  Used for alpha and beta release.

    Documentation is generated by using the Libdoc tool.
    """
    if version:
        out = Path(f"docs/KeePassLibrary-{version}.html")
    else:
        out = Path("docs/KeePassLibrary.html")
    libdoc(str(Path("src/KeePassLibrary")), str(out))


@task
def set_version(ctx, version):
    """Set project version in `src/KeePassLibrary/__init__.py`` file.

    Args:
        version: Project version to set or ``dev`` to set development version.

    Following PEP-440 compatible version numbers are supported:
    - Final version like 3.0 or 3.1.2.
    - Alpha, beta or release candidate with ``a``, ``b`` or ``rc`` postfix,
      respectively, and an incremented number like 3.0a1 or 3.0.1rc1.
    - Development version with ``.dev`` postfix and an incremented number like
      3.0.dev1 or 3.1a1.dev2.

    When the given version is ``dev``, the existing version number is updated
    to the next suitable development version. For example, 3.0 -> 3.0.1.dev1,
    3.1.1 -> 3.1.2.dev1, 3.2a1 -> 3.2a2.dev1, 3.2.dev1 -> 3.2.dev2.
    """
    version = Version(version, VERSION_PATH, VERSION_PATTERN)
    version.write()
    print(version)


@task
def print_version(ctx):
    """Print the current project version."""
    print(Version(path=VERSION_PATH))


@task
def tidy(ctx):
    """Runs robottidy for project atest code."""
    ctx.run("robotidy atests/")


@task
def lint(ctx):
    """Runs flake8 for project Python code."""
    ctx.run("flake8 --config .flake8 tasks.py src/ atests/ utests/")


@task
def utest(ctx):
    ctx.run("pytest ./utests/")


@task
def atest(ctx):
    ctx.run("robot -d .results atests")


@task(pre=[clean])
def build(ctx):
    ctx.run("python -m build --sdist --wheel")
