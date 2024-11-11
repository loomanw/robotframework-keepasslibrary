*** Settings ***
Documentation       Check Group related keywords

Library             KeePassLibrary
Library             Collections
Library             DateTime

Test Setup          Open Keepass Database    ${KEEPASS_DATABASE}    ${KEEPASS_PASSWORD}    ${KEEPASS_KEYFILE}
Test Teardown       Close Keepass Database

Test Tags           group


*** Variables ***
${DATADIR}              ${CURDIR}${/}Data${/}
${KEEPASS_DATABASE}     ${DATADIR}test4.kdbx
${KEEPASS_KEYFILE}      ${DATADIR}test4.key
${KEEPASS_PASSWORD}     password


*** Test Cases ***
Get Created Time
    [Documentation]    Selected group contains expected created time properties.
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True   
    ${mtime}=    Get Group Created Time    ${group}
    Should Be Equal As Integers    ${mtime.year}           2017
    Should Be Equal As Integers    ${mtime.month}          3
    Should Be Equal As Integers    ${mtime.day}            13
    Should Be Equal As Integers    ${mtime.hour}           1
    Should Be Equal As Integers    ${mtime.minute}         8
    Should Be Equal As Integers    ${mtime.second}         13
    Should Be Equal As Integers    ${mtime.microsecond}    0 
    Should Be Equal As Strings     ${mtime.tzinfo}         UTC

Get Expiry Time
    [Documentation]    Selected group contains expected expiry time properties.
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${mtime}=    Get Group Expiry Time    ${group}
    Should Be Equal As Integers    ${mtime.year}           2017
    Should Be Equal As Integers    ${mtime.month}          3
    Should Be Equal As Integers    ${mtime.day}            13
    Should Be Equal As Integers    ${mtime.hour}           1
    Should Be Equal As Integers    ${mtime.minute}         8
    Should Be Equal As Integers    ${mtime.second}         13
    Should Be Equal As Integers    ${mtime.microsecond}    0 
    Should Be Equal As Strings     ${mtime.tzinfo}         UTC

Get Expires
    [Documentation]    Selected group contains expected expires
    [Tags]    set
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    ${FALSE}
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${value}=    Get Group Expires    ${group}
    Should Be Equal    ${value_expected}    ${value}

Get Expired
    [Documentation]    Selected group contains expected expired
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    False
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${value}=    Get Group Expired    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Entries
    [Documentation]    Selected group contains expected entries
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    @{values_expected}=    Create List    group_entry    foobar_entry
    @{values}=    Create List
    ${group}=    Get Groups By Name    ${group_name}    first=True
    @{entries}=    Get Group Entries    ${group}
    FOR    ${entry}    IN    @{entries}
        ${title}=    Get Entry Title    ${entry}
        Append To List    ${values}    ${title}
    END
    Lists Should Be Equal    ${values_expected}    ${values}

Get Icon
    [Documentation]    Selected group contains expected icon
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    1
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${value}=    Get Group Icon    ${group}
    Should Be Equal As Integers    ${value_expected}    ${value}

Get Is Root Group
    [Documentation]    Selected group contains expected root group flag
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    False
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${value}=    Get Group Is Root Group    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Last Accessed Time
    [Documentation]    Selected entry contains expected last accessed time properties.
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True  
    ${mtime}=    Get Group Accessed Time    ${group}
    Should Be Equal As Integers    ${mtime.year}           2020
    Should Be Equal As Integers    ${mtime.month}          10
    Should Be Equal As Integers    ${mtime.day}            24
    Should Be Equal As Integers    ${mtime.hour}           14
    Should Be Equal As Integers    ${mtime.minute}         16
    Should Be Equal As Integers    ${mtime.second}         38
    Should Be Equal As Integers    ${mtime.microsecond}    0 
    Should Be Equal As Strings     ${mtime.tzinfo}         UTC

Get Modified Time
    [Documentation]    Selected entry contains expected modified time properties.
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True 
    ${mtime}=    Get Group Modified Time    ${group}
    Should Be Equal As Integers    ${mtime.year}           2017
    Should Be Equal As Integers    ${mtime.month}          3
    Should Be Equal As Integers    ${mtime.day}            13
    Should Be Equal As Integers    ${mtime.hour}           1
    Should Be Equal As Integers    ${mtime.minute}         8
    Should Be Equal As Integers    ${mtime.second}         43
    Should Be Equal As Integers    ${mtime.microsecond}    0 
    Should Be Equal As Strings     ${mtime.tzinfo}         UTC

Get Name
    [Documentation]    Selected group contains expected rname
    [Tags]    get
    ${group_uuid}=    Set Variable    95155a32-5317-a10f-d4e4-d0c2030264b6
    ${value_expected}=    Set Variable    foobar_group
    ${group}=    Get Groups By Uuid    ${group_uuid}    first=True
    ${value}=    Get Group Name    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Notes
    [Documentation]    Selected group contains expected uuid
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    group notes
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${value}=    Get Group Notes    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Parent Group
    [Documentation]    Selected group contains expected parent group
    [Tags]    get
    ${group_name}=    Set Variable    subgroup
    ${value_expected}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${parent}=    Get Group Parent    ${group}
    ${value}=    Get Group Name    ${parent}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Path
    [Documentation]    Selected group contains expected path
    [Tags]    get
    ${group_name}=    Set Variable    subgroup
    ${value_expected}=    Set Variable    foobar_group/subgroup
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${value}=    Get Group Path    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Subgroups
    [Documentation]    Selected group contains expected subgroups
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    @{values_expected}=    Create List    subgroup
    @{values}=    Create List
    ${group}=    Get Groups By Name    ${group_name}    first=True
    @{subgroups}=    Get Group Subgroups    ${group}
    FOR    ${subgroup}    IN    @{subgroups}
        ${name}=    Get Group Name    ${subgroup}
        Append To List    ${values}    ${name}
    END
    Lists Should Be Equal    ${values_expected}    ${values}

Get Uuid
    [Documentation]    Selected group contains expected uuid
    [Tags]    get
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    95155a32-5317-a10f-d4e4-d0c2030264b6
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${value}=    Get Group Uuid    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}

Group Should Be Expired
    [Documentation]    Selected group should be expired.
    [Tags]    should be
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True   
    Set Group Expires    ${group}     ${TRUE} 
    Group Should Be Expired    ${group}

Group Should Not Be Expired
    [Documentation]    Selected entry should not be expired.
    [Tags]    should not be
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True   
    Set Group Expires    ${group}     ${FALSE} 
    Group Should Not Be Expired    ${group}

Set Accessed Time
    [Documentation]    Selected group accessed time property can be set with a datetime object.
    [Tags]    set
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True   
    ${mtime1}=    Get Group Accessed Time    ${group}    UTC
    ${value}=    Convert Date    2014-06-11 10:07:42.123    datetime
    Set Group Accessed Time    ${group}    ${value}    local
    ${mtime2}=    Get Group Accessed Time    ${group}
    Should Not Be Equal    ${mtime1}    ${mtime2}    

Set Created Time
    [Documentation]    Selected group created time property can be set with a datetime object.
    [Tags]    set
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True   
    ${mtime1}=    Get Group Created Time    ${group}    UTC
    ${datetime}=    Convert Date    2014-06-11 10:07:42.123    datetime
    Set Group Created Time    ${group}    ${datetime}    local    
    ${mtime2}=    Get Group Created Time    ${group}
    Should Not Be Equal    ${mtime1}    ${mtime2} 

Set Expires
    [Documentation]    Selected group expires can be set
    [Tags]    set
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    ${TRUE}
    ${group}=    Get Groups By Name    ${group_name}    first=True
    Set Group Expires    ${group}    ${value_expected}
    ${value}=    Get Group Expires    ${group}
    Should Be Equal    ${value_expected}    ${value}

Set Expiry Time
    [Documentation]    Selected entry expiry time property can be set with a datetime object.
    [Tags]    set
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True   
    ${mtime1}=    Get Group Expiry Time    ${group}    UTC
    ${datetime}=    Convert Date    2014-06-11 10:07:42.123    datetime
    Set Group Expiry Time    ${group}    ${datetime}    local
    ${mtime2}=    Get Group Expiry Time    ${group}
    Should Not Be Equal    ${mtime1}    ${mtime2} 

Set Icon
    [Documentation]    Selected group notes can be set
    [Tags]    set
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    20
    ${group}=    Get Groups By Name    ${group_name}    first=True
    Set Group Icon    ${group}    ${value_expected}
    ${value}=    Get Group Icon    ${group}
    Should Be Equal As Integers    ${value_expected}    ${value}

Set Name
    [Documentation]    Selected group name can be set
    [Tags]    set
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    foobar_group_new
    ${group}=    Get Groups By Name    ${group_name}    first=True
    Set Group Name    ${group}    ${value_expected}
    ${value}=    Get Group Name    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Notes
    [Documentation]    Selected group notes can be set
    [Tags]    set
    ${group_name}=    Set Variable    foobar_group
    ${value_expected}=    Set Variable    new_notes
    ${group}=    Get Groups By Name    ${group_name}    first=True
    Set Group Notes    ${group}    ${value_expected}
    ${value}=    Get Group Notes    ${group}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Modified Time
    [Documentation]    Selected entry modified time property can be set with a datetime object.
    [Tags]    set
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True   
    ${mtime1}=    Get Group Modified Time    ${group}    UTC
    ${datetime}=    Convert Date    2014-06-11 10:07:42.123    datetime
    Set Group Modified Time    ${group}    ${datetime}    local
    ${mtime2}=    Get Group Modified Time    ${group}
    Should Not Be Equal    ${mtime1}    ${mtime2}

Touch Modify False
    [Documentation]    Selected group is touched and not modified
    [Tags]    touch
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${atime1}=    Get Group Accessed Time   ${group}
    ${mtime1}=    Get Group Modified Time    ${group}
    ${ctime1}=    Get Group Created Time    ${group}
    Touch Group    ${group}    False
    ${atime2}=    Get Group Accessed Time    ${group}
    ${mtime2}=    Get Group Modified Time    ${group}
    ${ctime2}=    Get Group Created Time    ${group}
    Should Not Be Equal    ${atime1}    ${atime2}         
    Should Be Equal    ${mtime1}    ${mtime2}         
    Should Be Equal    ${ctime1}    ${ctime2}         

Touch Modify True
    [Documentation]    Selected group is touched and modified
    [Tags]    touch
    ${group_name}=    Set Variable    foobar_group
    ${group}=    Get Groups By Name    ${group_name}    first=True
    ${atime1}=    Get Group Accessed Time   ${group}
    ${mtime1}=    Get Group Modified Time    ${group}
    ${ctime1}=    Get Group Created Time    ${group}
    Touch Group    ${group}    True
    ${atime2}=    Get Group Accessed Time    ${group}
    ${mtime2}=    Get Group Modified Time    ${group}
    ${ctime2}=    Get Group Created Time    ${group}
    Should Not Be Equal    ${atime1}    ${atime2}         
    Should Not Be Equal    ${mtime1}    ${mtime2}         
    Should Be Equal    ${ctime1}    ${ctime2} 
