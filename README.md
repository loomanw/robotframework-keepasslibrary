
# KeePass Library

This library enables Robot Framework to interact with KeePass databases.

[![Python package](https://github.com/loomanw/robotframework-keepasslibrary/actions/workflows/python-package.yml/badge.svg)](https://github.com/loomanw/robotframework-keepasslibrary/actions/workflows/python-package.yml) 
[![Version](https://img.shields.io/pypi/v/robotframework-keepasslibrary.svg?label=version)](https://github.com/loomanw/robotframework-keepasslibrary) 
![PyPI - License](https://img.shields.io/pypi/l/robotframework-keepasslibrary) 
![PyPI - Downloads](https://img.shields.io/pypi/dm/robotframework-keepasslibrary) 
[![Updates](https://pyup.io/repos/github/loomanw/robotframework-keepasslibrary/shield.svg)](https://pyup.io/repos/github/loomanw/robotframework-keepasslibrary)

Supported KeePass versions:
- KDBX3
- KDBX4
    
KeepassLibrary uses the [PyKeePass](https://pypi.org/project/pykeepass/) modules internally to access KeePass databases
    
See https://keepass.info for more information about KeePass in general

---
### Keyword Documentation
See [keyword documentation](https://loomanw.github.io/robotframework-keepasslibrary/KeePassLibrary.html) for available keywords and more information about the library in general.

---
### Installation
The recommended approach to install KeePassLibrary, regardless the version, is using  [pip](http://pip-installer.org/).

Install (or upgrade) the latest KeePassLibrary version:

    pip install --upgrade robotframework-keepasslibrary

---
### Example

```robotframework
*** Settings ***
Documentation     A test suite with a single test for retrieving a password.
...
...               The test opens a KeePass database named Database.kdbx using 
...               the keyfile Database.key. 
...               It then retrieves the first entry that matches the Username "User Name"
...               and logs the password from the returned KeePass database entry
Library           KeePassLibrary

*** Test Cases ***
Get KeePass Database Entry
    Open KeePass Database       Database.kdbx    keyfile=Database.key        
    ${entry}=    Get Entries By Username    User Name    first=True
    ${value}=    Get Entry Password    ${entry}  
    Log     Password for User Name is ${value}
```

---
### Versions:
 - `0.4.0` Update dependencies, rework for pykeepas 4.x with keyfile v2 support, additional test cases 
 - `0.3.1` Update dependencies, tests moved to github actions 
 - `0.3.0` New keywords for accessing entry and group data, rebuild of code using [Python Library Core](https://github.com/robotframework/PythonLibCore).
 - `0.2.5` Fix manifest, additional test cases
 - `0.2.4` Update dependencies
 - `0.2.3` Update dependencies, new travis builds
 - `0.2.2` Update dependencies
 - `0.2.1` KDBX v3 and v4 test cases
 - `0.2.0` Group Support
 - `0.1.0` Entry Support
