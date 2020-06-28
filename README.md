
# KeePass Library

This library enables Robot Framework to interact with KeePass databases.

[![Build Status](https://travis-ci.org/loomanw/robotframework-keepasslibrary.svg?branch=master)](https://travis-ci.org/loomanw/robotframework-keepasslibrary)
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
### Versions:
 - `0.2.5` Fix manifest, additional test cases
 - `0.2.4` Update dependencies
 - `0.2.3` Update dependencies, new travis builds
 - `0.2.2` Update dependencies
 - `0.2.1` KDBX v3 and v4 test cases
 - `0.2.0` Group Support
 - `0.1.0` Entry Support

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
...               The test loads a KeePass database named Database.kdbx using 
...               the keyfile Database.key. 
...               It then retrieves the first entry that matches the Username "User Name"
...               and logs the password from the returned KeePass database entry
Import            KeePassLibrary

*** Test Cases ***
Get KeePass Database Entry
    Get KeePass Database       Database.kdbx    keyfile=Database.key        
    ${entry}=   Get Entries By Username    User Name    first=True  
    Log     Password for spam_user is ${entry.password}
```

