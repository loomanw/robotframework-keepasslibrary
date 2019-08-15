# KeePass Library

This library enables Robot Framework to interact with KeePass databases.

Supported KeePass versions:
- KDBX3
- KDBX4
    
KeepassLibrary uses the [PyKeePass](https://pypi.org/project/pykeepass/) modules internally to access KeePass databases
    
See https://keepass.info for more information about KeePass in general

----
### Versions:

<<<<<<< HEAD
0.1.0   Alpha
=======
0.2.0 Group Support
0.1.0 Entry Support 
>>>>>>> develop
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
<<<<<<< HEAD
...               The test loads a KeePass database named example.kbx using 
...               the keyfile example.key. 
...               It then retrieves the first entry that matches the Username spam_user
=======
...               The test loads a KeePass database named Database.kdbx using 
...               the keyfile Database.key. 
...               It then retrieves the first entry that matches the Username "User Name"
>>>>>>> develop
...               and logs the password from the returned KeePass database entry
Import            KeePassLibrary

*** Test Cases ***
Get KeePass Database Entry
    Get KeePass Database       Database.kdbx    keyfile=Database.key        
    ${entry}=	Get Entries By Username    User Name    first=True	
	Log 	Password for spam_user is ${entry.password}
```

