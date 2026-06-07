=====================
KeePassLibrary 0.12.0
=====================

Most important enhancements
===========================
- Support for Robot Framework 7.4 Secret variable type
- Implemented Mypy static type checker
- New TimeZone enum replacing str
- Refactoring argument names
- Documentation Datatypes TimeZone, RegExpFlags, Entry, Group
- Documentation tagged keywords

Changed keywords
----------------

==================================  ====================================================
Keyword                             Change
==================================  ====================================================
Create Keepass Database             New keyword
Add Group                           New keyword
Add Entry                           New keyword
Open Keepass Database               Support for Robot Framework 7.4 Secret variable type
Set Entry Password                  Support for Robot Framework 7.4 Secret variable type
Get Entry Password                  Support for Robot Framework 7.4 Secret variable type
Get Groups By Name                  Argument name change: group_name -> name
Get Groups By Path                  Argument name change: group_path_str -> path
Get Entry Accessed Time             TimeZone enum replacing str
Set Entry Accessed Time             TimeZone enum replacing str
Get Entry Created Time              TimeZone enum replacing str
Set Entry Created Time              TimeZone enum replacing str
Get Entry Expiry Time               TimeZone enum replacing str
Set Entry Expiry Time               TimeZone enum replacing str
Get Entry Modified Time             TimeZone enum replacing str
Set Entry Modified Time             TimeZone enum replacing str
Get Group Accessed Time             TimeZone enum replacing str
Set Group Accessed Time             TimeZone enum replacing str
Get Group Created Time              TimeZone enum replacing str
Set Group Created Time              TimeZone enum replacing str
Get Group Expiry Time               TimeZone enum replacing str
Set Group Expiry Time               TimeZone enum replacing str
Get Group Modified Time             TimeZone enum replacing str
Set Group Modified Time             TimeZone enum replacing str
==================================  =================================================