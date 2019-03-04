import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

# Declare the classifiers
CLASSIFIERS = '''
Development Status :: 3 - Alpha
License :: OSI Approved :: MIT License  
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Security :: Cryptography  
Topic :: Software Development :: Quality Assurance
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()

# Get the version from
with open(join(CURDIR, 'KeePassLibrary', 'KeePassLibrary.py')) as f:
    VERSION = re.search("\n__version__ = '(.*)'", f.read()).group(1)

# Get the long description from the README file
with open(join(CURDIR, 'README.md')) as f:
    DESCRIPTION = f.read()

# Get install requires from requirements.txt
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name                            = "robotframework-keepasslibrary",
    version                         = VERSION,
    author                          = "William Looman",
    author_email                    = "wlooman@gmail.com",
    description                     = "Robot Framework library for working with KeePass Database",
    long_description                = DESCRIPTION,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/loomanw/robotframework-keepasslibrary",
    packages                        = find_packages(),
    classifiers                     = CLASSIFIERS,
    install_requires                = REQUIREMENTS,
)