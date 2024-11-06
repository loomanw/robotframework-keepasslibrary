from os.path import abspath, dirname, join
import re

from setuptools import setup, find_packages


CURDIR = dirname(abspath(__file__))

# Declare the classifiers
CLASSIFIERS = '''
Development Status :: 3 - Alpha
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Programming Language :: Python :: 3 :: Only
Topic :: Security :: Cryptography
Topic :: Software Development :: Quality Assurance
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()

# Get the version from
with open(join(CURDIR, 'src', 'KeePassLibrary', '__init__.py')) as f:
    VERSION = re.search("\n__version__ = '(.*)'", f.read()).group(1)

# Get the long description from the README file
with open(join(CURDIR, 'README.md')) as f:
    DESCRIPTION = f.read()

# Get install requires from requirements.txt
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()


setup(
    name                            = "robotframework-keepasslibrary",  # noqa: E251, E221
    version                         = VERSION,  # noqa: E251, E221
    author                          = "William Looman",  # noqa: E251, E221
    author_email                    = "wlooman@gmail.com",  # noqa: E251, E221
    description                     = "Robot Framework library for working with KeePass Database",  # noqa: E251, E221
    long_description                = DESCRIPTION,  # noqa: E251, E221
    long_description_content_type   = "text/markdown",  # noqa: E251, E221
    url                             = "https://github.com/loomanw/robotframework-keepasslibrary",  # noqa: E251, E221
    classifiers                     = CLASSIFIERS,  # noqa: E251, E221
    python_requires                 = '>=3.8, <4',  # noqa: E251, E221
    install_requires                = REQUIREMENTS,  # noqa: E251, E221
    package_dir                     = {'': 'src'},  # noqa: E251, E221
    packages                        = find_packages('src'),  # noqa: E251, E221
    package_data                    = {  # noqa: E251, E221
        'KeePassLibrary':
            ['*.pyi']
    }
)
