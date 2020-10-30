====================
KeePassLibrary 0.3.0
====================

Most important enhancements
===========================

Better architecture
-------------------

Implementation of the Robot Framework PythonLibCore.

The new architecture should not change how the keywords are used in Robot
Framework test data. 

__ https://github.com/robotframework/PythonLibCore


Deprecated keywords
-------------------

==================================  =================================================  =======
       Deprecated keyword                             Use instead                      Issue
==================================  =================================================  =======
Close Database                      Close Keepass Database
Save                                Save Keepass Database
Load Database                       Open Keepass Database

==================================  =================================================  =======

New Keywords
------------

==================================  
        New keyword                 
==================================  
Close Keepass Database
Get Entry Custom Properties
Get Entry Custom Property
Get Entry Expired
Get Entry Expires
Get Entry Icon
Get Entry Notes
Get Entry Password
Get Entry Tags
Get Entry Title
Get Entry Url
Get Entry Username
Get Entry Uuid
Get Group Entries
Get Group Expired
Get Group Expires
Get Group Icon
Get Group Is Root Group
Get Group Name
Get Group Notes
Get Group Parent
Get Group Path
Get Group Subgroups
Get Group Uuid
Open Keepass Database
Remove Entry Custom Property
Set Entry Custom Property
Set Entry Expires
Set Entry Icon
Set Entry Notes
Set Entry Password
Set Entry Tags
Set Entry Title
Set Entry Url
Set Entry Username
Set Group Expires
Set Group Icon
Set Group Name
Set Group Notes
Save Keepass Database
==================================  