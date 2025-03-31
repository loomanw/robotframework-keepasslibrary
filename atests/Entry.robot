*** Settings ***
Documentation       Check Entry related keywords

Library             KeePassLibrary
Library             Collections
Library             DateTime
Library             String

Test Setup          Open Keepass Database    ${KEEPASS_DATABASE}    ${KEEPASS_PASSWORD}    ${KEEPASS_KEYFILE}
Test Teardown       Close Keepass Database

Test Tags           entry


*** Variables ***
${DATADIR}              ${CURDIR}${/}Data${/}
${KEEPASS_DATABASE}     ${DATADIR}test4.kdbx
${KEEPASS_KEYFILE}      ${DATADIR}test4.key
${KEEPASS_PASSWORD}     password


*** Test Cases ***
Entry Should Be Expired
    [Documentation]    Selected entry should be expired.
    [Tags]    should be
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    Set Entry Expires    ${entry}     ${TRUE} 
    Entry Should Be Expired    ${entry}

Entry Should Not Be Expired
    [Documentation]    Selected entry should not be expired.
    [Tags]    should not be
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    Set Entry Expires    ${entry}     ${FALSE} 
    Entry Should Not Be Expired    ${entry}
    
Get Created Time
    [Documentation]    Selected entry contains expected created time properties.
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    ${mtime}=    Get Entry Created Time    ${entry}
    Should Be Equal As Integers    ${mtime.year}            2017
    Should Be Equal As Integers    ${mtime.month}           3
    Should Be Equal As Integers    ${mtime.day}             13
    Should Be Equal As Integers    ${mtime.hour}            1
    Should Be Equal As Integers    ${mtime.minute}          8
    Should Be Equal As Integers    ${mtime.second}          46
    Should Be Equal As Integers    ${mtime.microsecond}     0 
    Should Be Equal As Strings     ${mtime.tzinfo}          UTC

Get Custom Properties
    [Documentation]    Selected entry contains expected custom properties.
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Create Dictionary    foobar_attribute=foobar
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Custom Properties    ${entry}
    Dictionaries Should Be Equal    ${value_expected}    ${value}

Get Custom Property
    [Documentation]    Selected entry contains expected custom property
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${entry_property_key}=    Set Variable    foobar_attribute
    ${value_expected}=    Set Variable    foobar
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Custom Property    ${entry}    ${entry_property_key}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Expired
    [Documentation]    Selected entry contains expected expired
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    False
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Expired    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Expires
    [Documentation]    Selected entry contains expected expires
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    False
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Expires    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Expiry Time
    [Documentation]    Selected entry contains expected expiry time properties.
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    ${mtime}=    Get Entry Expiry Time    ${entry}
    Should Be Equal As Integers    ${mtime.year}           2017
    Should Be Equal As Integers    ${mtime.month}          3
    Should Be Equal As Integers    ${mtime.day}            13
    Should Be Equal As Integers    ${mtime.hour}           1
    Should Be Equal As Integers    ${mtime.minute}         8
    Should Be Equal As Integers    ${mtime.second}         46
    Should Be Equal As Integers    ${mtime.microsecond}    0 
    Should Be Equal As Strings     ${mtime.tzinfo}         UTC

Get Last Access Time
    [Documentation]    Selected entry contains expected last access time properties.
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    ${mtime}=    Get Entry Accessed Time    ${entry}
    Should Be Equal As Integers    ${mtime.year}           2020
    Should Be Equal As Integers    ${mtime.month}          10
    Should Be Equal As Integers    ${mtime.day}            24
    Should Be Equal As Integers    ${mtime.hour}           13
    Should Be Equal As Integers    ${mtime.minute}         2
    Should Be Equal As Integers    ${mtime.second}         6
    Should Be Equal As Integers    ${mtime.microsecond}    0 
    Should Be Equal As Strings     ${mtime.tzinfo}         UTC

Get Modified Time
    [Documentation]    Selected entry contains expected modified time properties.
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    ${mtime}=    Get Entry Modified Time    ${entry}
    Should Be Equal As Integers    ${mtime.year}            2020
    Should Be Equal As Integers    ${mtime.month}           10
    Should Be Equal As Integers    ${mtime.day}             24
    Should Be Equal As Integers    ${mtime.hour}            12
    Should Be Equal As Integers    ${mtime.minute}          15
    Should Be Equal As Integers    ${mtime.second}          54
    Should Be Equal As Integers    ${mtime.microsecond}     0 
    Should Be Equal As Strings     ${mtime.tzinfo}          UTC

Get Icon
    [Documentation]    Selected entry contains expected icon
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    0
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Icon    ${entry}
    Should Be Equal As Integers    ${value_expected}    ${value}

Get Notes
    [Documentation]    Selected entry contains expected icon
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    root entry notes
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Notes    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Pasword
    [Documentation]    Selected entry contains expected password
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    passw0rd
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Password    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Tags
    [Documentation]    Selected entry contains expected tags
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Create List
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Tags    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Title
    [Documentation]    Selected entry contains expected title
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    ${entry_title}
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Title    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get URL
    [Documentation]    Selected entry contains expected URL
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    http://example.com
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Url    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Username
    [Documentation]    Selected entry contains expected username
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    foobar_user
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Username    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Get Uuid
    [Documentation]    Selected entry contains expected uuid
    [Tags]    get
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    eb90914e-5dd3-8f78-9669-dd1fb39791dc
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${value}=    Get Entry Uuid    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Accessed Time
    [Documentation]    Selected entry accessed time property can be set with a datetime object.
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    ${mtime1}=    Get Entry Accessed Time    ${entry}    UTC
    ${value}=    Convert Date    2014-06-11 10:07:42.123    datetime
    Set Entry Accessed Time    ${entry}    ${value}    local
    ${mtime2}=    Get Entry Accessed Time    ${entry}
    Should Not Be Equal    ${mtime1}    ${mtime2}    

Set Custom Property Existing
    [Documentation]    Selected entry custom porperty (existing) can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${custom_property_key}=    Set Variable    foobar_attribute
    ${value_expected}=    Set Variable    new_value
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Custom Property    ${entry}    ${custom_property_key}    ${value_expected}
    ${value}=    Get Entry Custom Property    ${entry}    ${custom_property_key}
    Should Be Equal    ${value_expected}    ${value}

Set Custom Property New
    [Documentation]    Selected entry custom porperty (new) can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${custom_property_key}=    Set Variable    new_key
    ${value_expected}=    Set Variable    new_value
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Custom Property    ${entry}    ${custom_property_key}    ${value_expected}
    ${value}=    Get Entry Custom Property    ${entry}    ${custom_property_key}
    Should Be Equal    ${value_expected}    ${value}

Set Created Time
    [Documentation]    Selected entry created time property can be set with a datetime object.
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    ${mtime1}=    Get Entry Created Time    ${entry}    UTC
    ${value}=    Convert Date    2014-06-11 10:07:42.123    datetime
    Set Entry Created Time    ${entry}    ${value}    local
    ${mtime2}=    Get Entry Created Time    ${entry}
    Should Not Be Equal    ${mtime1}    ${mtime2} 

Set Expires
    [Documentation]    Selected entry expires can be set with a boolean
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    ${TRUE}
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Expires    ${entry}    ${value_expected}
    ${value}=    Get Entry Expires    ${entry}
    Should Be Equal    ${value_expected}    ${value}

Set Expiry Time
    [Documentation]    Selected entry expiry time property can be set with a datetime object.
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    ${mtime1}=    Get Entry Expiry Time    ${entry}    UTC
    ${value}=    Convert Date    2014-06-11 10:07:42.123    datetime
    Set Entry Expiry Time    ${entry}    ${value}    local
    ${mtime2}=    Get Entry Expiry Time    ${entry}
    Should Not Be Equal    ${mtime1}    ${mtime2} 

Set Icon
    [Documentation]    Selected entry icon can be set with a integer
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    10
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Icon    ${entry}    ${value_expected}
    ${value}=    Get Entry Icon    ${entry}
    Should Be Equal As Integers    ${value_expected}    ${value}

Set Modified Time
    [Documentation]    Selected entry modified time property can be set with a datetime object.
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True   
    ${mtime1}=    Get Entry Modified Time    ${entry}    UTC
    ${value}=    Convert Date    2014-06-11 10:07:42.123    datetime
    Set Entry Modified Time    ${entry}    ${value}    local
    ${mtime2}=    Get Entry Modified Time    ${entry}
    Should Not Be Equal    ${mtime1}    ${mtime2}    

Set Notes
    [Documentation]    Selected entry notes can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    very important\nnotes\nfor this entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Notes    ${entry}    ${value_expected}
    ${value}=    Get Entry Notes    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Password
    [Documentation]    Selected entry passowrd can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    P@$$w0rd
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Password    ${entry}    ${value_expected}
    ${value}=    Get Entry Password    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Tags With List
    [Documentation]    Selected entry tags can be set with a list
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Create List    tag1    tag2
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Tags    ${entry}    ${value_expected}
    ${value}=    Get Entry Tags    ${entry}
    Lists Should Be Equal    ${value_expected}    ${value}

Set Tags With String
    [Documentation]    Selected entry tags can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    tag1;tag2
    ${list_expected}=    Create List    tag1    tag2
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Tags    ${entry}    ${value_expected}
    ${value}=    Get Entry Tags    ${entry}
    Lists Should Be Equal    ${list_expected}    ${value}

Set Title
    [Documentation]    Selected entry title can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    new title
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Title    ${entry}    ${value_expected}
    ${value}=    Get Entry Title    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set URL
    [Documentation]    Selected entry url can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    http://pypi.org
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Url    ${entry}    ${value_expected}
    ${value}=    Get Entry Url    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Set Username
    [Documentation]    Selected entry username can be set with a string
    [Tags]    set
    ${entry_title}=    Set Variable    root_entry
    ${value_expected}=    Set Variable    set_foobar_user
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    Set Entry Username    ${entry}    ${value_expected}
    ${value}=    Get Entry Username    ${entry}
    Should Be Equal As Strings    ${value_expected}    ${value}

Touch Modify False
    [Documentation]    Selected entry is touched and not modified
    [Tags]    touch
    ${entry_title}=    Set Variable    root_entry
    ${entry}=     Get Entries By Title    ${entry_title}    first=True   
    ${atime1}=    Get Entry Accessed Time    ${entry}
    ${mtime1}=    Get Entry Modified Time    ${entry}
    ${ctime1}=    Get Entry Created Time    ${entry}
    Touch Entry   ${entry}    False
    ${atime2}=    Get Entry Accessed Time    ${entry}
    ${mtime2}=    Get Entry Modified Time    ${entry}
    ${ctime2}=    Get Entry Created Time    ${entry}
    Should Not Be Equal    ${atime1}    ${atime2}         
    Should Be Equal    ${mtime1}    ${mtime2}         
    Should Be Equal    ${ctime1}    ${ctime2}         

Touch Modify True
    [Documentation]    Selected entry is touched and modified
    [Tags]    touch
    ${entry_title}=    Set Variable    root_entry
    ${entry}=     Get Entries By Title    ${entry_title}    first=True   
    ${atime1}=    Get Entry Accessed Time    ${entry}
    ${mtime1}=    Get Entry Modified Time    ${entry}
    ${ctime1}=    Get Entry Created Time    ${entry}
    Touch Entry    ${entry}    True
    ${atime2}=    Get Entry Accessed Time    ${entry}
    ${mtime2}=    Get Entry Modified Time    ${entry}
    ${ctime2}=    Get Entry Created Time    ${entry}
    Should Not Be Equal    ${atime1}    ${atime2}         
    Should Not Be Equal    ${mtime1}    ${mtime2}         
    Should Be Equal    ${ctime1}    ${ctime2}

List Attachments
    [Documentation]    Listing existing attachment succeeds
    [Tags]    attachment
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${attachment_spam}    Encode String To Bytes    spam spam    UTF-8
    ${attachment_eggs}    Encode String To Bytes    egg egg    UTF-8
    Set Entry Attachment    ${entry}    spam.txt    ${attachment_spam}
    Set Entry Attachment    ${entry}    eggs.txt    ${attachment_eggs}
    ${attachments}=    Get Entry Attachments    ${entry}
    Length Should Be    ${attachments}    2
    List Should Contain Value    ${attachments}    spam.txt
    List Should Contain Value    ${attachments}    eggs.txt

Add New Attachment
    [Documentation]    Adding a new attachment succeeds
    [Tags]    set    attachment
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${string_set}=       Set Variable    spam spam
    ${attachment_set}    Encode String To Bytes    ${string_set}    UTF-8
    Set Entry Attachment    ${entry}    spam.txt    ${attachment_set}
    ${attachment_get}    Get Entry Attachment    ${entry}    spam.txt
    Should Be Equal    ${attachment_get}    ${attachment_set}
    ${string_get}    Decode Bytes To String    ${attachment_get}    UTF-8
    Should Be Equal As Strings    ${string_get}    ${string_set}

Get Existing Attachment
    [Documentation]    Get existing attachment succeeds
    [Tags]    get    attachment
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${string_set}=     Set Variable    spam spam
    ${attachment_set}    Encode String To Bytes    ${string_set}      UTF-8
    Set Entry Attachment    ${entry}    spam.txt    ${attachment_set}
    ${attachment_get}    Get Entry Attachment    ${entry}    spam.txt
    Should Be Equal    ${attachment_get}    ${attachment_set}
    ${string_get}    Decode Bytes To String    ${attachment_get}    UTF-8
    Should Be Equal As Strings    ${string_get}    ${string_set}

Replace Existing Attachment
    [Documentation]    Replace existing attachment succeeds
    [Tags]    set    attachment
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${string_set}=     Set Variable    spam spam
    ${string_set2}=    Set Variable    spam spam spam
    ${attachment_set}    Encode String To Bytes    ${string_set}      UTF-8
    ${attachment_set2}    Encode String To Bytes    ${string_set2}    UTF-8
    Set Entry Attachment    ${entry}    spam.txt    ${attachment_set}
    ${attachment_get}    Get Entry Attachment    ${entry}    spam.txt
    Should Be Equal    ${attachment_get}    ${attachment_set}
    Set Entry Attachment    ${entry}    spam.txt    ${attachment_set2}
    ${attachment_get}    Get Entry Attachment    ${entry}    spam.txt
    Should Be Equal    ${attachment_get}    ${attachment_set2}
    ${string_get}    Decode Bytes To String    ${attachment_get}    UTF-8
    Should Be Equal As Strings    ${string_get}    ${string_set2}

Remove Existing Attachment Succes
    [Documentation]    Removing entry attachment succeeds
    [Tags]    remove    attachment
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${string_set}=     Set Variable    spam spam
    ${binary_set}=    Encode String To Bytes    ${string_set}      UTF-8
    Set Entry Attachment    ${entry}    spam.txt    ${binary_set}
    ${attachments}=    Get Entry Attachments    ${entry}
    Length Should Be    ${attachments}    1
    Remove Entry Attachment    ${entry}    spam.txt
    ${attachments}=    Get Entry Attachments    ${entry}
    Length Should Be    ${attachments}    0

Remove Existing Attachment Fail
    [Documentation]    Removing entry attachment succeeds
    [Tags]    remove    attachment
    ${entry_title}=    Set Variable    root_entry
    ${entry}=    Get Entries By Title    ${entry_title}    first=True
    ${error_msg}=                  Set Variable     No attachment with provided filename 'spam.txt'.
    Run Keyword And Expect Error   ${error_msg}     Remove Entry Attachment    ${entry}    spam.txt

Attachment Should Be Present Succes
    [Documentation]    Selected entry should contain attachment succeeds
    [Tags]    should be    attachment
    ${entry} =                         Get Entries By Title    root_entry    first=True
    ${string_set}=                     Set Variable    Attachment contents
    ${binary_set} =                    Encode String To Bytes    ${string_set}    UTF-8
    Set Entry Attachment               ${entry}    spam.txt      ${binary_set}
    Entry Should Contain Attachment    ${entry}    spam.txt

Attachment Should Be Present Fail
    [Documentation]    Selected entry should contain attachment fails
    [Tags]    should be    attachment
    ${entry} =                     Get Entries By Title    root_entry    first=True
    ${error_msg}=                  Set Variable     The entry should contain attachment 'spam.txt', but it does not.
    Run Keyword And Expect Error   ${error_msg}     Entry Should Contain Attachment    ${entry}    spam.txt

Attachment Should Not Be Present Succes
    [Documentation]    Selected entry should not contain attachment succeeds
    [Tags]    should not be    attachment
    ${entry} =                         Get Entries By Title    root_entry    first=True
    Entry Should Not Contain Attachment    ${entry}    spam.txt

Attachment Should Not Be Present Fail
    [Documentation]    Selected entry should contain attachment fails
    [Tags]    should not be    attachment
    ${entry} =                     Get Entries By Title    root_entry    first=True
    ${string_set}=                 Set Variable    Attachment contents
    ${binary_set} =                Encode String To Bytes    ${string_set}    UTF-8
    Set Entry Attachment               ${entry}    spam.txt      ${binary_set}
    ${error_msg}=                  Set Variable     The entry should not contain attachment 'spam.txt', but it does.
    Run Keyword And Expect Error   ${error_msg}     Entry Should Not Contain Attachment    ${entry}    spam.txt
